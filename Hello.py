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
import time

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        initial_sidebar_state="collapsed"
    )

    questions = {1:"Question 1",
             2:"Question 2",
             3:"Question 3",
             4:"Question 4",
             5:"Question 5",
             6:"Question 6"}

    answers = {1:"Answer 1",
            2:"Answer 2",
            3:"Answer 3",
            4:"Answer 4",
            5:"Answer 5",
            6:"Answer 6"}

    hint_level_1 = {1:"Hint 1 Level 1",
                    2:"Hint 2 Level 1",
                    3:"Hint 3 Level 1",
                    4:"Hint 4 Level 1",
                    5:"Hint 5 Level 1",
                    6:"Hint 6 Level 1"}

    hint_level_2 = {1:"Hint 1 Level 2",
                    2:"Hint 2 Level 2",
                    3:"Hint 3 Level 2",
                    4:"Hint 4 Level 2",
                    5:"Hint 5 Level 2",
                    6:"Hint 6 Level 2"}
    
    images = {1:"./Question 1.jpg",
              2:"./Question 2.jpg",
              3:"./Question 3.jpg",
              4:"./Question 4.jpg",
              5:"./Question 5.jpg",
              6:"./Question 6.jpg"}

    if "progress" not in st.session_state:
        st.session_state.progress = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {1:"",
                                    2:"",
                                    3:"",
                                    4:"",
                                    5:"",
                                    6:""}
        

    st.write("# This is an example of an escape room")
    if st.session_state.progress == 0:
        st.image("./IMG_0125.png")
        if st.button("Start Escape Room"):
            st.session_state.progress = 1
            st.rerun()
    
    elif st.session_state.progress > 6:
        st.write("Congratulations! You've Escaped!")
        if st.button("Restart Escape Room"):
            st.session_state.progress = 1
            st.rerun()

    else:
        st.write(questions[st.session_state.progress])
        st.image(images[st.session_state.progress])
        time.sleep(0.5)
        st.session_state.answers[st.session_state.progress] = st.text_input("Enter your answer", st.session_state.answers[st.session_state.progress])
        if st.button("Submit answer"):
            if st.session_state.answers[st.session_state.progress] == answers[st.session_state.progress]:
                st.write("Correct!!")
            else:
                st.write("Your answer " + st.session_state.answers[st.session_state.progress] + " is incorrect! Try Again or look at the hits below!")
        if st.button("Next Question"):
            if st.session_state.answers[st.session_state.progress] == answers[st.session_state.progress]:
                st.session_state.progress = st.session_state.progress + 1
                st.rerun()
            else:
                st.write("You can't move forward")
                st.rerun()
        if st.button("Previous Question"):
            if st.session_state.progress > 1:
                st.session_state.progress = st.session_state.progress - 1
                st.rerun()
            else:
                st.session_state.progress = 0
                st.rerun()
        if st.session_state.progress > 0:
            with st.expander("Hint Level 1"):
                st.write(hint_level_1[st.session_state.progress])
            with st.expander("Hint Level 2"):
                st.write(hint_level_2[st.session_state.progress])



    # st.write("Question 1: abcdefg")
    # answer_1 = st.text_input("Enter your answer to question 1")
    # if st.button("Submit answer 1"):
    #     if answer_1 == "test":
    #         st.write("Correct!")
    #         st.session_state.progress = 1
    #     else:
    #         st.write("Wrong. Hint 1")

    # if st.session_state.progress > 0:
    #     st.write("Question 2: abcdefg")
    #     answer_2 = st.text_input("Enter your answer to question 2")
    #     if st.button("Submit answer 2"):
    #         if answer_2 == "test123":
    #             st.write("Correct!")
    #             st.session_state.progress = 2
    #         else:
    #             st.write("Wrong. Hint 2")
    
    # if st.session_state.progress > 1:
    #     st.write("Congrats! You done")


if __name__ == "__main__":
    run()
