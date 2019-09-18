# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# --------------------------------------------------------------------------
"""The decorator to apply if you want the given function traced."""

import functools

import azure.core.tracing.common as common
from azure.core.settings import settings

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    from typing import Callable, Any


def distributed_trace_async(func=None, name_of_span=None):
    # type: (Callable, str) -> Callable[[Any], Any]
    if func is None:
        return functools.partial(distributed_trace_async, name_of_span=name_of_span)

    @functools.wraps(func)
    async def wrapper_use_tracer(*args, **kwargs):
        # type: (Any, Any) -> Any
        merge_span = kwargs.pop('merge_span', False)
        passed_in_parent = kwargs.pop("parent_span", None)

        span_impl_type = settings.tracing_implementation()
        if span_impl_type is None:
            return await func(*args, **kwargs) # type: ignore

        # Merge span is parameter is set, but only if no explicit parent are passed
        if merge_span and not passed_in_parent:
            return await func(*args, **kwargs) # type: ignore

        with common.change_context(passed_in_parent):
            name = name_of_span or common.get_function_and_class_name(func, *args)  # type: str
            with span_impl_type(name=name):
                return await func(*args, **kwargs)  # type: ignore

    return wrapper_use_tracer
