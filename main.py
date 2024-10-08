import streamlit as st
import random

# Define the questions and answers
questions = [
    {"question": "What is the name of the main character in the game 'The Last of Us'?", "answer": "Ellie"},
    {"question": "Which game is known for its iconic character 'Master Chief'?", "answer": "Halo"},
    {"question": "What is the name of the popular mobile game where you have to swipe to match candies?", "answer": "Candy Crush"},
    {"question": "Which game is set in the fictional world of Spira?", "answer": "Final Fantasy X"},
    {"question": "What is the name of the game where you have to build and manage your own city?", "answer": "SimCity"},
    {"question": "Which game is known for its fast-paced action and 'Devil Trigger' ability?", "answer": "Devil May Cry"},
    {"question": "What is the name of the game where you have to solve puzzles to progress through a mysterious world?", "answer": "Portal"},
    {"question": "Which game is set in the world of Azeroth?", "answer": "World of Warcraft"},
    {"question": "What is the name of the game where you have to collect resources and build structures to survive?", "answer": "Minecraft"},
    {"question": "Which game is known for its 'parkour' mechanics and futuristic setting?", "answer": "Mirror's Edge"},
    {"question": "What is the name of the game where you have to control a character with a 'Portal Gun'?", "answer": "Portal 2"},
    {"question": "Which game is set in the world of Tamriel?", "answer": "The Elder Scrolls V: Skyrim"},
    {"question": "What is the name of the game where you have to build and manage your own theme park?", "answer": "RollerCoaster Tycoon"},
    {"question": "Which game is known for its 'stealth' mechanics and protagonist 'Solid Snake'?", "answer": "Metal Gear Solid"},
    {"question": "What is the name of the game where you have to collect 'Power Stars' to progress?", "answer": "Super Mario 64"},
    {"question": "Which game is set in the world of Pandora?", "answer": "Borderlands"},
    {"question": "What is the name of the game where you have to control a character with a 'BFG'?", "answer": "Doom"},
    {"question": "Which game is known for its 'survival horror' elements and protagonist 'Leon S. Kennedy'?", "answer": "Resident Evil 4"},
    {"question": "What is the name of the game where you have to build and manage your own civilization?", "answer": "Civilization VI"},
    {"question": "Which game is set in the world of Rapture?", "answer": "BioShock"},
    {"question": "What is the name of the game where you have to control a character with a 'Gravity Gun'?", "answer": "Half-Life 2"},
    {"question": "Which game is known for its 'open-world' design and protagonist 'Niko Bellic'?", "answer": "Grand Theft Auto IV"},
    {"question": "What is the name of the game where you have to collect 'Chaos Emeralds' to progress?", "answer": "Sonic the Hedgehog"},
    {"question": "Which game is set in the world of Thedas?", "answer": "Dragon Age: Inquisition"},
    {"question": "What is the name of the game where you have to control a character with a 'Lightsaber'?", "answer": "Star Wars: Knights of the Old Republic"}
]

# Initialize session state
if 'selected_questions' not in st.session_state:
    st.session_state.selected_questions = random.sample(questions, 10)  # Randomly select 10 questions
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0  # Start with the first question
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False  # Initialize answer visibility

# Function to get the current question
def get_current_question():
    return st.session_state.selected_questions[st.session_state.question_index]

# Styling the Streamlit app
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ff7e5f, #feb47b); /* Gradient background */
        font-family: 'Arial', sans-serif;
        height: 100vh; /* Ensure the gradient covers the entire viewport */
        margin: 0;
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center content vertically */
        align-items: center; /* Center content horizontally */
    }
    .title {
        font-size: 50px;
        color: #fff; /* White color for better contrast */
        font-weight: bold;
        margin: 20px 0;
        text-shadow: 2px 2px 4px #aaa;
    }
    .question {
        font-size: 24px;
        margin: 20px 0;
        text-align: center;
        color: #fff; /* White color for better contrast */
        animation: fadeIn 1s ease-in;
    }
    .next-button, .show-answer-button {
        display: block;
        width: 100%;
        background-color: #32cd32;
        color: white;
        font-size: 20px;
        padding: 10px 0;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        margin-top: 20px;
        transition: background-color 0.3s;
    }
    .next-button:hover, .show-answer-button:hover {
        background-color: #28a745;
    }
    .end-message {
        text-align: center;
        font-size: 28px;
        color: #fff; /* White color for better contrast */
        margin-top: 30px;
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Title of the quiz
st.markdown('<h1 class="title">GAMEHOLICS QUIZ</h1>', unsafe_allow_html=True)

# Check if the quiz is finished
if st.session_state.question_index < len(st.session_state.selected_questions):
    # Display current question with serial number
    question_number = st.session_state.question_index + 1  # Serial number starts from 1
    current_question = get_current_question()
    st.markdown(f'<div class="question">Question {question_number}: {current_question["question"]}</div>',
                 unsafe_allow_html=True)

    # Button to show the answer
    if st.button("Show Answer"):
        st.session_state.show_answer = True  # Reveal the answer

    # Display the answer if it has been revealed
    if st.session_state.show_answer:
        st.markdown(f'<div class="question">Answer: {current_question["answer"]}</div>', unsafe_allow_html=True)

    # Button to get the next question
    if st.button("Next"):
        # Move to the next question only if the answer is shown
        if st.session_state.show_answer:
            st.session_state.question_index += 1
            st.session_state.show_answer = False  # Reset answer visibility for the next question
        else:
            st.markdown('<div class="question"></div>', unsafe_allow_html=True)

else:
    # Display end message
    st.markdown('<div class="end-message">GAME OVER</div>', unsafe_allow_html=True)