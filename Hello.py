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

    # questions = {1:"Question 1",
    #          2:"Question 2",
    #          3:"Question 3",
    #          4:"Question 4",
    #          5:"Question 5",
    #          6:"Question 6"}

    # answers = {1:"Answer 1",
    #         2:"Answer 2",
    #         3:"Answer 3",
    #         4:"Answer 4",
    #         5:"Answer 5",
    #         6:"Answer 6"}

    # hint_level_1 = {1:"Hint 1 Level 1",
    #                 2:"Hint 2 Level 1",
    #                 3:"Hint 3 Level 1",
    #                 4:"Hint 4 Level 1",
    #                 5:"Hint 5 Level 1",
    #                 6:"Hint 6 Level 1"}

    # hint_level_2 = {1:"Hint 1 Level 2",
    #                 2:"Hint 2 Level 2",
    #                 3:"Hint 3 Level 2",
    #                 4:"Hint 4 Level 2",
    #                 5:"Hint 5 Level 2",
    #                 6:"Hint 6 Level 2"}
    
    # images = {1:"./Question 1.jpg",
    #           2:"./Question 2.jpg",
    #           3:"./Question 3.jpg",
    #           4:"./Question 4.jpg",
    #           5:"./Question 5.jpg",
    #           6:"./Question 6.jpg"}

    # if "progress" not in st.session_state:
    #     st.session_state.progress = 0

    # if "answers" not in st.session_state:
    #     st.session_state.answers = {1:"",
    #                                 2:"",
    #                                 3:"",
    #                                 4:"",
    #                                 5:"",
    #                                 6:""}
        

    # st.write("# This is an example of an escape room")
    # if st.session_state.progress == 0:
    #     st.image("./IMG_0125.png")
    #     if st.button("Start Escape Room"):
    #         st.session_state.progress = 1
    #         st.rerun()
    
    # elif st.session_state.progress > 6:
    #     st.write("Congratulations! You've Escaped!")
    #     if st.button("Restart Escape Room"):
    #         st.session_state.progress = 1
    #         st.rerun()

    # else:
    #     st.write(questions[st.session_state.progress])
    #     st.image(images[st.session_state.progress])
    #     time.sleep(0.5)
    #     st.session_state.answers[st.session_state.progress] = st.text_input("Enter your answer", st.session_state.answers[st.session_state.progress])
    #     if st.button("Submit answer"):
    #         if st.session_state.answers[st.session_state.progress] == answers[st.session_state.progress]:
    #             st.write("Correct!!")
    #         else:
    #             st.write("Your answer " + st.session_state.answers[st.session_state.progress] + " is incorrect! Try Again or look at the hits below!")
    #     if st.button("Next Question"):
    #         if st.session_state.answers[st.session_state.progress] == answers[st.session_state.progress]:
    #             st.session_state.progress = st.session_state.progress + 1
    #             st.rerun()
    #         else:
    #             st.write("You can't move forward")
    #             st.rerun()
    #     if st.button("Previous Question"):
    #         if st.session_state.progress > 1:
    #             st.session_state.progress = st.session_state.progress - 1
    #             st.rerun()
    #         else:
    #             st.session_state.progress = 0
    #             st.rerun()
    #     if st.session_state.progress > 0:
    #         with st.expander("Hint Level 1"):
    #             st.write(hint_level_1[st.session_state.progress])
    #         with st.expander("Hint Level 2"):
    #             st.write(hint_level_2[st.session_state.progress])

    if "progress" not in st.session_state:
        st.session_state.progress = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {1:"",
                                    2:"",
                                    3:"",
                                    4:"",
                                    5:"",
                                    6:"",
                                    7:"",
                                    8:"",
                                    9:"",
                                    10:"",
                                    11:"",
                                    12:"",}

    questions = [
        {"empty":"placeholder"},
        {
            "question": "Q1/12: You're taking the bus on your way back home. It's been a loooong day, what are you thinking about?",
            "image": "images/Q1.gif",
            "answers": {
                "option1": {
                    "text": "I'm just so tired and can't wait to go home. Why does everyday feel the same...",
                    "scores": { "T": 0, "F": 1 },
                },
                "option2": {
                    "text": "Should I rest or work first when I get home? Most importantly, what's for dinner?",
                    "scores": { "T": 1, "F": 0 },
                },
            },
        },
        {
            "question": "Q2/12: You look outside the windows, seems like it's going to rain soon. Suddenly everything turns into darkness!!",
            "image": "images/Q2.gif",
            "answers": {
                "option1": {
                    "text": "I don't remember this tunnel. *Pull out your phone to look at the map*",
                    "scores": { "P": 0, "J": 1 },
                },
                "option2": {
                    "text": "*Turn around to see the other's reaction* Should I ask the driver what's going on?",
                    "scores": { "P": 1, "J": 0 },
                },
            },
        },
        {
            "question": "Q3/12: Before you can do anything, the bus stops and everything around you floats up!",
            "image": "images/Q3.gif",
            "answers": {
                "option1": {
                    "text": "Ok this is weird, am I dreaming? *pinch your arm*",
                    "scores": { "S": 1, "N": 0 },
                },
                "option2": {
                    "text": "Is this a prank? Am I getting kidnapped by aliens?!",
                    "scores": { "S": 0, "N": 1 },
                },
            },
        },
        {
            "question": "Q4/12: Amidst the surprise, your eyes catch something drifting past the window.",
            "image": "images/Q4.gif",
            "answers": {
                "option1": {
                    "text": "Woahhh...so many cats! How cute!! I wanna give them a hug!",
                    "scores": { "T": 0, "F": 1 },
                },
                "option2": {
                    "text": "Cats? In space? That's kinda odd... How do they survive out there?!",
                    "scores": { "T": 1, "F": 0 },
                },
            },
        },
        {
            "question": "Q5/12: 'Welcome Aboard!' a small robot appears and announces, 'We will reach our destination in 5 months 6 days and 2 hours!'",
            "image": "images/Q5.gif",
            "answers": {
                "option1": {
                    "text": "Cool! A space cruise?! Where are we going? Do I get a spacesuit? This is so exciting!",
                    "scores": { "P": 1, "J": 0 },
                },
                "option2": {
                    "text": "Hey uh...Am I in space? How did I get here? When can I go home?! Why..",
                    "scores": { "P": 0, "J": 1 },
                },
            },
        },
        {
            "question": "Q6/12: The robot just points to the back of the bus which now looks more like inside of a spaceship! What do you want to see first?",
            "image": "images/Q6.gif",
            "answers": {
                "option1": {
                    "text": "Solar system themed fountain in the middle. I want to take pictures with it.",
                    "scores": { "I": 0, "E": 1 },
                },
                "option2": {
                    "text": "Cozy corner with a massaging chair. I need to sit down and process.",
                    "scores": { "I": 1, "E": 0 },
                },
            },
        },
        {
            "question": "Q7/12: On the way back to your seat, you are surrounded by cats! 'Unauthorized passenger detected, CAPTURE CAPTURE!'",
            "image": "images/Q7.gif",
            "answers": {
                "option1": {
                    "text": "Woah! What do you mean unauthorized? I'm the passenger of this cruise!",
                    "scores": { "S": 1, "N": 0 }
                },
                "option2": {
                    "text": "Ok, I have no idea what's going on. How about we calm down and chat for a bit?",
                    "scores": { "S": 0, "N": 1 },
                },
            },
        },
        {
            "question": "Q8/12: Suddenly, the robot glides in, it whispers something to the cats that makes them stop.",
            "image": "images/Q8.gif",
            "answers": {
                "option1": {
                    "text": "Bob!! Thank you! You come to save me, right?",
                    "scores": { "E": 1, "I": 0 },
                },
                "option2": {
                    "text": "HA! That's right! Back off, cats! Am I safe to go now?!",
                    "scores": { "E": 0, "I": 1 },
                },
            },
        },
        {
            "question": "Q9/12: The robot transforms into a giant vacuum cleaner, the cats use it to point at you!",
            "image": "images/Q9.gif",
            "answers": {
                "option1": {
                    "text": "Throw your coat at them as distraction, run towards the big green 'EXIT' sign!",
                    "scores": { "J": 1, "P": 0 },
                },
                "option2": {
                    "text": "Run in random direction, confuse them, blend in with the crowd!",
                    "scores": { "J": 0, "P": 1 },
                },
            },
        },
        {
            "question": "Q10/12: You run past the gift shop. Looks like you got rid of them. It wouldn't hurt to get some souvenirs, right?",
            "image": "images/Q10.gif",
            "answers": {
                "option1": {
                    "text": "Get the Jupiter headphone, wear it to hear people's thoughts!",
                    "scores": { "F": 1, "T": 0 },
                },
                "option2": {
                    "text": "Get the Mars watch, turn it and you can time travel!",
                    "scores": { "F": 0, "T": +1 },
                },
            },

        },
        {
            "question": "Q11/12: The giant vacuum cleaner suddenly emerges in front of you! You're sucked into its vortex!!!",
            "image": "images/Q11.gif",
            "answers": {
                "option1": {
                    "text": "It's ok, this is just a dream! I'll wake up soon! *close your eyes and give up*",
                    "scores": { "S": 1, "N": 0 },
                },
                "option2": {
                    "text": "I'll find the way out! Maybe there are some secret doors! *look around for the way out*",
                    "scores": { "S": 0, "N": 1 },
                },
            },
        },
        {
            "question": "Q12/12: After a moment of darkness, you find yourself back in the bus. 'Are you alright?' the ticket inspector asks",
            "image": "images/Q12.gif",
            "answers": {
                "option1": {
                    "text": "Woah! I thought I was captured... Nevermind! I'm alright now, I guess? *panic in silence*",
                    "scores": { "E": 0, "I": 1 },
                },
                "option2": {
                    "text": "You won't believe it...I think I just had the wildest dream ever! *tell him about your space adventure*",
                    "scores": { "E": 1, "I": 0 },
                },
            },
        },
        {
            "question": "When you look up again, the inspector's already gone. You glance outside the window, darkness creeps in as the bus enters another tunnel...",
            "image": "images/Q13.gif",
            "answers": {
                "option1": {
                    "text": "Wait...was that Bob?",
                },
                "option2": {
                    "text": "Oh no...Do I have to go through this again?",
                },
            },
        },
    ]

    resultOptions = {
        "ISTJ": {
            "image": "1DE.png",
        },
        "ISFJ": {
            "image": "2light.png"
        },
        "INFJ": {
            "image": "3UFO.png"
        },
        "INTJ": {
            "image": "4nebula.png"
        },
        "ISTP": {
            "image": "5comet.png"
        },
        "ISFP": {
            "image": "6ST.png"
        },
        "INFP": {
            "image": "7DM.png"
        },
        "INTP": {
            "image": "8met.png"
        },
        "ESTP": {
            "image": "9BH.png"
        },
        "ESFP": {
            "image": "10Sn.png"
        },
        "ENFP": {
            "image": "11Grav.png"
        },
        "ENTP": {
            "image": "12hand.png"
        },
        "ESTJ": {
            "image": "13sat.png"
        },
        "ESFJ": {
            "image": "14sun.png"
        },
        "ENFJ": {
            "image": "15gal.png"
        },
        "ENTJ": {
            "image": "16rocket.png"
        },
    }

    # Go through all the scores and find the personality
    def calculate_results(answers):
        result = {}
        personality = ""
        for answer in answers.keys():
            for attribute in answer.keys():
                if attribute not in result.keys():
                    result.update({attribute:answer[attribute]})
                else:
                    result[attribute] = result[attribute] + answer[attribute]

        if result["I"] > result["E"]:
            personality += "I"
        else:
            personality += "E"
        if result["N"] > result["S"]:
            personality += "N"
        else:
            personality += "S"
        if result["T"] > result["F"]:
            personality += "T"
        else:
            personality += "F"
        if result["P"] > result["J"]:
            personality += "P"
        else:
            personality += "J"

        return personality


    st.write("# This is an example of an escape room")
    if st.session_state.progress == 0:
        st.image("./IMG_0125.png")
        if st.button("Start Escape Room"):
            st.session_state.progress = 1
            st.rerun()
    
    elif st.session_state.progress > 12:
        st.write("Congratulations! You've Escaped!")
        personality = calculate_results(st.session_state.answers)
        st.write(personality)
        if st.button("Restart Escape Room"):
            st.session_state.progress = 1
            st.rerun()

    else:
        st.write(questions[st.session_state.progress]['question'])
        # st.image(questions[st.session_state.progress]['image'])
        st.write(questions[st.session_state.progress]['image']) # Write image name for now instead of showing image
        time.sleep(0.5)
        if st.button(questions[st.session_state.progress]['answers']['option1']['text']):
            st.session_state.answers[st.session_state.progress] = questions[st.session_state.progress]['answers']['option1']['scores']
            st.session_state.progress = st.session_state.progress + 1
            st.rerun()
        if st.button(questions[st.session_state.progress]['answers']['option2']['text']):
            st.session_state.answers[st.session_state.progress] = questions[st.session_state.progress]['answers']['option1']['scores']
            st.session_state.progress = st.session_state.progress + 1
            st.rerun()
        if st.button("Previous Question"):
            if st.session_state.progress > 1:
                st.session_state.progress = st.session_state.progress - 1
                st.rerun()
            else:
                st.session_state.progress = 0
                st.rerun()

if __name__ == "__main__":
    run()
