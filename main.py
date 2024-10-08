import streamlit as st
import random

# Define the questions and answers
questions = [
    {"question": "What is the name of the main character in the game 'The Last of Us'?", "answer": "Ellie"},
    {"question": "Which game is known for its iconic character 'Master Chief'?", "answer": "Halo"},
    {"question": "What is the name of the game where you control a character with a 'Lightsaber'?", "answer": "Star Wars: Knights of the Old Republic"},
    {"question": "What battle royale game features a shrinking play area and is developed by Krafton?", "answer": "PUBG: Battlegrounds"},
    {"question": "Which MOBA game is developed by Riot Games and features champions with unique abilities?", "answer": "League of Legends"},
    {"question": "What survival game allows players to craft, build, and survive against zombies?", "answer": "Minecraft"},
    {"question": "What is the name of the tactical shooter that emphasizes teamwork and strategy, developed by Ubisoft?", "answer": "Rainbow Six Siege"},
    {"question": "Which open-world RPG features Geralt of Rivia as the main character?", "answer": "The Witcher 3: Wild Hunt"},
    {"question": "In which game do players hunt monsters in a vast open world?", "answer": "Monster Hunter: World"},
    {"question": "What is the title of the life simulation game where players create and control people?", "answer": "The Sims 4"},
    {"question": "What horror game features a group of players trying to survive against a killer?", "answer": "Dead by Daylight"},
    {"question": "Which game is known for its realistic driving physics and extensive car customization?", "answer": "Forza Horizon"},
    {"question": "What game features characters from the One Piece universe in a mobile format?", "answer": "One Piece Treasure Cruise"},
    {"question": "In which RPG do players explore a vast fantasy world and engage in turn-based combat?", "answer": "Genshin Impact"},
    {"question": "Which racing game is known for its arcade-style gameplay and open-world design?", "answer": "Forza Horizon 5"},
    {"question": "What is the name of the rhythm-based VR game that lets players slash blocks to the beat of music?", "answer": "Beat Saber"},
    {"question": "Which game developed by Epic Games allows players to build structures while competing in a battle royale?", "answer": "Fortnite"},
    {"question": "What is the title of the tactical shooter featuring hero characters and team-based gameplay?", "answer": "Valorant"},
    {"question": "Which space exploration game allows players to build bases on different planets?", "answer": "No Man's Sky"},
    {"question": "What mobile game involves matching colorful candies to progress through levels?", "answer": "Candy Crush Saga"},
    {"question": "Which narrative-driven game lets players make choices that affect the story?", "answer": "Life is Strange"},
    {"question": "What strategy game allows players to build and manage a civilization from the Stone Age to the Information Age?", "answer": "Age of Empires IV"},
    {"question": "In which multiplayer game do players explore a post-apocalyptic world filled with infected humans?", "answer": "The Last of Us Part II"},
    {"question": "What is the name of the mobile battle royale game developed by Tencent?", "answer": "Call of Duty: Mobile"},
    {"question": "Which card game is set in the Magic: The Gathering universe?", "answer": "Magic: The Gathering Arena"},
    {"question": "In which game do players team up in squads to compete in tactical matches in a futuristic world?", "answer": "Apex Legends"}
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
