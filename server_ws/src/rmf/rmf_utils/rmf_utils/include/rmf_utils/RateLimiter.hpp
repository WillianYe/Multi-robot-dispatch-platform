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

#ifndef RMF_UTILS__RATELIMITER_HPP
#define RMF_UTILS__RATELIMITER_HPP

#include <chrono>

#include <rmf_utils/impl_ptr.hpp>

namespace rmf_utils {

//==============================================================================
/// A class used to track limits in the rate at which an event may occur. A
/// counter will increment each time reached_limit() is called within a time
/// period.
///
/// If the counter reaches its limit then reached_limit() will return true.
///
/// If the counter has not reached its limit then reached_limit() will return
/// false.
///
/// If reached_limit() is called again after the period limit has passed, then
/// the time period will be reset and the function will return false.
class RateLimiter
{
public:

  /// Constructor
  ///
  /// \param[in] period_limit_
  ///   How long between events before the counter is reset to zero
  ///
  /// \param[in] count_limit_
  ///   How high the counter can reach before check() returns false
  ///
  RateLimiter(
    std::chrono::steady_clock::duration period_limit_,
    std::size_t count_limit_);

  bool reached_limit() const;

  std::chrono::steady_clock::duration period_limit() const;
  RateLimiter& period_limit(std::chrono::steady_clock::duration new_limit);

  std::size_t count_limit() const;
  RateLimiter& count_limit(std::size_t new_limit);

  class Implementation;
private:
  rmf_utils::impl_ptr<Implementation> _pimpl;
};

} // namespace rmf_utils

#endif // RMF_UTILS__RATELIMITER_HPP
