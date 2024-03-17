# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    progress = {"qn1":False,
                "qn2":False}
    st.write("# This is an example of an escape room")

    st.write("Question 1: abcdefg")
    answer_1 = st.text_input("Enter your answer to question 1")
    if st.button("Submit answer 1"):
        if answer_1 == "test":
            st.write("Correct!")
            progress["qn1"]=True
        else:
            st.write("Wrong. Hint 1")

    if progress["qn1"]==True:
        st.write("Question 2: abcdefg")
        answer_2 = st.text_input("Enter your answer to question 2")
        if st.button("Submit answer 2"):
            if answer_2 == "test123":
                st.write("Correct!")
                progress["qn2"]=True
            else:
                st.write("Wrong. Hint 2")
    
    if progress["qn1"]==True & progress["qn2"]==True:
        st.write("Congrats! You done")

if __name__ == "__main__":
    run()
