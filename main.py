import streamlit as st
import random

# Define the questions and answers
questions = [
    {"question": "What is the name of the main character in the game 'The Last of Us'?", "answer": "Ellie"},
    {"question": "Which game features the iconic character 'Master Chief'?", "answer": "Halo"},
    {"question": "What is the name of the game series where you control a character with a 'Lightsaber'?", "answer": "Star Wars: Knights of the Old Republic"},
    {"question": "Which battle royale game was developed by Epic Games and became a cultural phenomenon?", "answer": "Fortnite"},
    {"question": "Which MOBA game developed by Riot Games features champions with unique abilities?", "answer": "League of Legends"},
    {"question": "What survival game allows players to craft, build, and explore in a blocky world?", "answer": "Minecraft"},
    {"question": "What tactical shooter developed by Ubisoft emphasizes teamwork and strategy?", "answer": "Rainbow Six Siege"},
    {"question": "Which open-world RPG features Geralt of Rivia as the main character?", "answer": "The Witcher 3: Wild Hunt"},
    {"question": "In which game do players hunt massive monsters in a fantasy world?", "answer": "Monster Hunter: World"},
    {"question": "What life simulation game allows players to create and control people in a virtual world?", "answer": "The Sims 4"},
    {"question": "What horror game features players trying to survive against a killer in an asymmetrical format?", "answer": "Dead by Daylight"},
    {"question": "Which racing game is known for its realistic driving physics and extensive car customization?", "answer": "Forza Horizon 5"},
    {"question": "What game based on the One Piece franchise features RPG elements and character collecting?", "answer": "One Piece Treasure Cruise"},
    {"question": "In which action RPG do players explore a vast open world and collect elemental characters?", "answer": "Genshin Impact"},
    {"question": "Which racing game allows players to explore a fictional version of Mexico in an open-world setting?", "answer": "Forza Horizon 5"},
    {"question": "What VR game lets players slash blocks to the beat of music using lightsabers?", "answer": "Beat Saber"},
    {"question": "Which game developed by Activision features a battle royale mode alongside traditional multiplayer?", "answer": "Call of Duty: Warzone"},
    {"question": "What tactical shooter features characters with unique abilities and is developed by Riot Games?", "answer": "Valorant"},
    {"question": "Which space exploration game allows players to build bases on procedurally generated planets?", "answer": "No Man's Sky"},
    {"question": "What mobile game involves matching colorful candies to complete levels?", "answer": "Candy Crush Saga"},
    {"question": "Which narrative-driven game allows players to make impactful choices that affect the story's outcome?", "answer": "Life is Strange"},
    {"question": "What strategy game allows players to build and manage a civilization through various historical eras?", "answer": "Civilization VI"},
    {"question": "In which multiplayer game do players explore a post-apocalyptic world filled with infected humans?", "answer": "The Last of Us Part II"},
    {"question": "What mobile battle royale game developed by Tencent features a variety of gameplay modes?", "answer": "PUBG Mobile"},
    {"question": "Which card game is set in the Magic: The Gathering universe and allows players to build decks?", "answer": "Magic: The Gathering Arena"},
    {"question": "In which game do players team up in squads to compete in tactical matches set in a futuristic environment?", "answer": "Apex Legends"}
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
        background: linear-gradient(90deg, #ff6a00, #ee0979); /* Gradient color for the title */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin: 20px 0;
        text-shadow: 2px 2px 4px #aaa;
        animation: slideIn 1s forwards; /* Slide in animation */
    }
    .question {
        font-size: 24px;
        margin: 20px 0;
        text-align: center;
        color: #00274d; /* Deep blue for a professional look */
        animation: fadeIn 1s ease-in;
    }
    .next-button, .show-answer-button {
        display: block;
        width: 200px; /* Fixed width for buttons */
        background-color: #32cd32;
        color: white;
        font-size: 20px;
        padding: 10px 0;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        margin-top: 20px;
        transition: background-color 0.3s, transform 0.3s; /* Add transform for hover */
    }
    .next-button:hover, .show-answer-button:hover {
        background-color: #28a745;
        transform: scale(1.05); /* Slightly increase size on hover */
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
    @keyframes slideIn {
        from { transform: translateY(-50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
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
    if st.button("Show Answer", key="show_answer_button"):
        st.session_state.show_answer = True  # Reveal the answer

    # Display the answer if it has been revealed
    if st.session_state.show_answer:
        st.markdown(f'<div class="question">Answer: {current_question["answer"]}</div>', unsafe_allow_html=True)

    # Button to get the next question
    if st.button("Next", key="next_button"):
        # Move to the next question only if the answer is shown
        if st.session_state.show_answer:
            st.session_state.question_index += 1
            st.session_state.show_answer = False  # Reset answer visibility for the next question
        else:
            st.markdown('<div class="question"></div>', unsafe_allow_html=True)

else:
    # Display end message
    st.markdown('<div class="end-message">GAME OVER</div>', unsafe_allow_html=True)
