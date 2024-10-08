import streamlit as st
import random

# Define the questions and answers
questions = [
    {"question": "What is the name of the game where players can build and explore in a blocky world?", "answer": "Minecraft"},
    {"question": "Which game features a battle royale mode with the goal of being the last player standing?", "answer": "Fortnite"},
    {"question": "In which game do players capture and train creatures called Pokémon?", "answer": "Pokémon"},
    {"question": "What racing game series includes characters like Mario and Luigi?", "answer": "Mario Kart"},
    {"question": "Which game involves solving puzzles and exploring dungeons to save Princess Zelda?", "answer": "The Legend of Zelda"},
    {"question": "What game allows players to create their own city and manage resources?", "answer": "SimCity"},
    {"question": "Who developed the popular mobile game 'Candy Crush Saga'?", "answer": "King"},
    {"question": "What game features characters competing in a virtual town called 'The Sims'?", "answer": "The Sims"},
    {"question": "Which game involves farming, crafting, and building a community?", "answer": "Stardew Valley"},
    {"question": "In which game do players race high-speed cars in various locations?", "answer": "Need for Speed"},
    {"question": "What game lets you play as a superhero swinging through a city?", "answer": "Spider-Man"},
    {"question": "Which game involves players teaming up to survive against zombies?", "answer": "Left 4 Dead"},
    {"question": "What classic game requires players to fill lines with falling blocks?", "answer": "Tetris"},
    {"question": "Who is the developer behind the 'Call of Duty' series?", "answer": "Activision"},
    {"question": "What game has you building and managing a farm with animals and crops?", "answer": "Farming Simulator"},
    {"question": "Which game lets players explore a fantasy world as a character named 'Geralt'?", "answer": "The Witcher 3: Wild Hunt"},
    {"question": "What game features a little bird flying through pipes?", "answer": "Flappy Bird"},
    {"question": "Which game is known for its colorful candies that players match to progress?", "answer": "Candy Crush Saga"},
    {"question": "In which multiplayer online battle arena game do two teams compete?", "answer": "League of Legends"},
    {"question": "What action RPG allows players to explore a vast world filled with dragons?", "answer": "Skyrim"},
    {"question": "What game features characters like Steve and Alex in a sandbox environment?", "answer": "Minecraft"},
    {"question": "Which mobile game has players building their own town and interacting with villagers?", "answer": "Animal Crossing: Pocket Camp"},
    {"question": "What game involves summoning monsters and casting spells in card battles?", "answer": "Magic: The Gathering Arena"},
    {"question": "What battle royale game features 100 players on an island with survival elements?", "answer": "PUBG Mobile"},
    {"question": "Which game has you racing against friends in colorful go-karts?", "answer": "Mario Kart"},
    {"question": "What mobile game has players tapping to shoot birds at green pigs?", "answer": "Angry Birds"},
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
        font-size: 40px; /* Scaled down size */
        background: linear-gradient(90deg, #ff6a00, #ee0979); /* Gradient color for the title */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin: 20px 0;
        text-shadow: 2px 2px 4px #aaa;
        text-align: center; /* Center the title */
        animation: slideIn 1s forwards; /* Slide in animation */
    }
    .question {
        font-size: 24px;
        margin: 20px 0;
        text-align: center;
        color: #003366; /* Dark blue for a formal look */
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
