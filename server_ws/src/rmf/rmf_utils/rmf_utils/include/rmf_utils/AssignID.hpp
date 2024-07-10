/*
 * Copyright (C) 2022 Open Source Robotics Foundation
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

#ifndef RMF_UTILS__ASSIGNID_HPP
#define RMF_UTILS__ASSIGNID_HPP

#include <atomic>

namespace rmf_utils {

//==============================================================================
template<typename T>
class AssignID
{
public:

  AssignID(T initial_value = 0)
  : _value(std::move(initial_value))
  {
    // Do nothing
  }

  T assign() const
  {
    return _value.fetch_add(1);
  }

  void fast_forward_to(const T desired_value) const
  {
    // TODO(MXG): We could give more consideration to what memory models we are
    // using in these atomic operations.
    auto current_value = _value.load();
    while (current_value < desired_value)
    {
      const bool success =
        _value.compare_exchange_weak(current_value, desired_value);

      if (success)
        return;

      current_value = _value.load();
    }
  }

private:
  mutable std::atomic<T> _value;
};

} // namespace rmf_utils

#endif // RMF_UTILS__ASSIGNID_HPP
