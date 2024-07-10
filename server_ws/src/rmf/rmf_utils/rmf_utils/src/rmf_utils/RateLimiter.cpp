/*
 * Copyright (C) 2021 Open Source Robotics Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/

#include <rmf_utils/RateLimiter.hpp>

#include <optional>

namespace rmf_utils {

//==============================================================================
class RateLimiter::Implementation
{
public:

  using Duration = std::chrono::steady_clock::duration;
  using Time = std::chrono::steady_clock::time_point;

  bool reached_limit() const
  {
    const auto now = std::chrono::steady_clock::now();
    if (!last_call.has_value() || *last_call + period_limit < now)
    {
      last_call = now;
      count = 1;
      return false;
    }

    ++count;
    return count_limit < count;
  }

  Duration period_limit;
  std::size_t count_limit;
  mutable std::size_t count = 0;
  mutable std::optional<Time> last_call = std::nullopt;
};

//==============================================================================
RateLimiter::RateLimiter(
  std::chrono::steady_clock::duration period_limit_,
  std::size_t count_limit_)
: _pimpl(rmf_utils::make_impl<Implementation>(
      Implementation{period_limit_, count_limit_}))
{
  // Do nothing
}

//==============================================================================
bool RateLimiter::reached_limit() const
{
  return _pimpl->reached_limit();
}

//==============================================================================
std::chrono::steady_clock::duration RateLimiter::period_limit() const
{
  return _pimpl->period_limit;
}

//==============================================================================
RateLimiter& RateLimiter::period_limit(std::chrono::steady_clock::duration l)
{
  _pimpl->period_limit = l;
  return *this;
}

//==============================================================================
std::size_t RateLimiter::count_limit() const
{
  return _pimpl->count_limit;
}

//==============================================================================
RateLimiter& RateLimiter::count_limit(std::size_t l)
{
  _pimpl->count_limit = l;
  return *this;
}

} // namespace rmf_utils
