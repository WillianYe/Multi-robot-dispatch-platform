/*
 * Copyright (C) 2019 Open Source Robotics Foundation
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

#include <rmf_utils/impl_ptr.hpp>
#include "TestClass.hpp"

#include <iostream>
#include <rmf_utils/catch.hpp>

TEST_CASE("Test impl_ptr")
{
  TestClass test("here is my test string");
  CHECK(test.get_test_text() == "here is my test string");

  TestClass copy{test};
  CHECK(test.get_test_text() == "here is my test string");

  TestClass moved = std::move(test);
  CHECK(moved.get_test_text() == "here is my test string");

  CHECK_FALSE(test._pimpl);

  test = TestClass("replacing the text");
  std::cout << test.get_test_text() << std::endl;

  CHECK(test.get_test_text() == "replacing the text");
}
