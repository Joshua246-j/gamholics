import streamlit as st
import random

# Define the URL of the background image
background_image_url = "https://images.unsplash.com/photo-1707858951210-1f3ae473606b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Define CSS for styling with animations and background
st.markdown(
    f"""
    <style>
    /* Apply the background image to the main container */
    [data-testid="stAppViewContainer"] {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Make the header background transparent to show the background image */
    [data-testid="stHeader"] {{
        background: transparent;
    }}

    /* Make the toolbar background transparent (optional) */
    [data-testid="stToolbar"] {{
        background: transparent;
    }}

    .title {{
        font-family: 'Permanent Marker', cursive;
        text-align: center;
        font-size: 48px; /* Increased font size for emphasis */
        font-weight: bold;
        margin-bottom: 20px;
        background: linear-gradient(to right, #FF6F20, #FFEA00); /* Bright gradient from orange to yellow */
        -webkit-background-clip: text; /* Clip the background to the text */
        -webkit-text-fill-color: transparent; /* Make the text transparent to show the gradient */
    }}

    .subtitle {{
        text-align: center;
        font-size: 18px; /* Increased font size for readability */
        font-weight: bold;
        margin-bottom: 20px;
        color: #FFD700; /* Gold color for attractiveness */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6); /* Shadow effect */
    }}

    .question {{
        color: #FFFFFF; /* Bright white for high contrast */
        font-size: 40px;
        margin-bottom: 10px;
        opacity: 0;
        animation: fadeIn 1s forwards;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6); /* Shadow effect */
    }}

    .answer {{
        color: #FFFFFF; /* Bright white for high contrast */
        font-size: 24px; /* Adjusted size for better readability */
        animation: fadeIn 1s forwards;
        background: linear-gradient(to right, #007FFF, #00BFFF); /* Bright electric blue gradient */
        -webkit-background-clip: text; /* Clip the background to the text */
        -webkit-text-fill-color: transparent; /* Make the text transparent to show the gradient */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6); /* Shadow effect */
    }}

    .success {{
        color: #27ae60; /* Green for success messages */
        font-weight: bold; /* Make success messages bold */
    }}

    .error {{
        color: #e74c3c; /* Red for error messages */
        font-weight: bold; /* Make error messages bold */
    }}

    .group-score {{
        font-size: 20px; /* Increased size for scores */
        color: #FFFFFF; /* White for group scores */
        font-weight: bold; /* Make scores bold */
        background: linear-gradient(to right, #FF6347, #FF4500); /* Light red to orange-red */
        -webkit-background-clip: text; /* Clip the background to the text */
        -webkit-text-fill-color: transparent; /* Make the text transparent to show the gradient */
    }}

    .final-score {{
        font-size: 22px; /* Increased size for final scores */
        color: #FFFFFF; /* White color for visibility */
        font-weight: bold;
        margin: 5px 0;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4); /* Shadow for depth */
    }}

    .winner {{
        font-size: 30px; /* Increased size for winners */
        color: #16a085; /* Teal for winners */
        text-align: center;
        margin-top: 15px;
        font-weight: bold;
        animation: zoomIn 1.5s forwards;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6); /* Shadow effect */
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    @keyframes zoomIn {{
        from {{ transform: scale(0.5); opacity: 0; }}
        to {{ transform: scale(1); opacity: 1; }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Define the questions for both rounds (25 questions each)
questions_round_1 = [
    {"question": "Which game features a cat that talks back to you?", "answer": "Talking tom"},
    {"question": "What endless running game involves dodging trains?", "answer": "Subway Surfers"},
    {"question": "In which racing game do you drive various cars to win races?", "answer": "Need for Speed"},
    {"question": "What strategy game allows you to build and upgrade a village?", "answer": "Clash of Clans"},
    {"question": "Which puzzle game involves matching candies?", "answer": "Candy Crush"},
    {"question": "What running game features an adventurous explorer navigating through temples?", "answer": "Temple Run"},
    {"question": "Which tactical shooter game has agents with unique abilities?", "answer": "Valorant"},
    {"question": "What battle royale game is set on a large island with survival elements?", "answer": "PUBG"},
    {"question": "Which mobile game has players battling against each other in squads?", "answer": "Free Fire"},
    {"question": "What game features colorful birds launching themselves at pigs?", "answer": "Angry Birds"},
    {"question": "Which sandbox game allows players to build and explore worlds made of blocks?", "answer": "Minecraft"},
    {"question": "In which farming simulator do you grow crops and raise animals?", "answer": "Stardew Valley"},
    {"question": "What game involves matching jewels in a grid to clear levels?", "answer": "Bejeweled"},
    {"question": "Which popular battle royale game features building structures?", "answer": "Fortnite"},
    {"question": "What classic puzzle game involves clearing lines of blocks?", "answer": "Tetris"},
    {"question": "Which game features creatures that battle each other using strategy?", "answer": "Pokemon"},
    {"question": "What mobile game involves launching birds to destroy structures?", "answer": "Angry Birds"},
    {"question": "Which game involves surviving on an island while gathering resources?", "answer": "ARK"},
    {"question": "What game lets players train virtual pets and battle them?", "answer": "Digimon"},
    {"question": "Which multiplayer online battle arena game features champions?", "answer": "League of Legends"},
    {"question": "What classic arcade game features a yellow character eating dots?", "answer": "Pac Man"},
    {"question": "In which game do players build their own empires in ancient times?", "answer": "Age of Empires"},
    {"question": "What role-playing game involves slaying dragons and completing quests?", "answer": "Skyrim"},
    {"question": "Which rhythm game lets players tap to the beat of popular songs?", "answer": "Beat Saber"},
    {"question": "What game features a boy and his dog exploring a vast open world?", "answer": "The Last Guardian"},
    {"question": "In which game do players collect and train monsters in a digital world?", "answer": "Monster Hunter"},
    {"question": "What survival horror game is set in a zombie-infested world?", "answer": "Resident Evil"},
    {"question": "Which virtual life simulation game allows players to create characters and build homes?", "answer": "The Sims"},
    {"question": "What game features a warrior fighting against mythical creatures?", "answer": "God of War"},
    {"question": "In which game do players create and manage a theme park?", "answer": "RollerCoaster Tycoon"},
    {"question": "What game involves solving mysteries as a detective?", "answer": "L.A. Noire"},
    {"question": "Which game allows players to create their own games within it?", "answer": "Roblox"},
    {"question": "What space exploration game lets players build and manage a spaceship?", "answer": "Kerbal Space Program"},
    {"question": "Which game is known for its battles between robots and players?", "answer": "Titanfall"},
    {"question": "What card game features iconic characters from various franchises?", "answer": "Hearthstone"},
    {"question": "In which game do players race each other using tiny toy cars?", "answer": "Micro Machines"},
    {"question": "What game involves battling zombies in a post-apocalyptic setting?", "answer": "Dying Light"},
    {"question": "Which game lets players take on the role of a criminal in a city?", "answer": "GTA"},
    {"question": "What simulation game involves managing a city and its inhabitants?", "answer": "SimCity"},
]

questions_round_2 = [
    {
        "question": "Which company developed the critically acclaimed game 'The Last of Us Part II'?",
        "answer": "Naughty Dog",
        "options": ["Naughty Dog", "Rockstar Games", "Ubisoft", "Electronic Arts"]
    },
    {
        "question": "Which game won the Game of the Year award at The Game Awards 2023?",
        "answer": "Baldur's Gate III",
        "options": ["Baldur's Gate III", "The Legend of Zelda: Tears of the Kingdom", "Starfield", "Resident Evil 4 Remake"]
    },
    {
        "question": "Who developed the game 'Red Dead Redemption 2'?",
        "answer": "Rockstar Games",
        "options": ["Rockstar Games", "CD Projekt Red", "Bethesda", "Insomniac Games"]
    },
    {
        "question": "Which company developed the tactical shooter game Valorant?",
        "answer": "Riot Games",
        "options": ["Riot Games", "Blizzard", "Activision", "Epic Games"]
    },
    {
        "question": "What game won the Best Ongoing Game award at The Game Awards 2022?",
        "answer": "Final Fantasy XIV",
        "options": ["Final Fantasy XIV", "Genshin Impact", "Fortnite", "Apex Legends"]
    },
    {
        "question": "What is considered the first-ever open-world game?",
        "answer": "Ultima I: The First Age of Darkness",
        "options": ["Ultima I: The First Age of Darkness", "The Legend of Zelda", "GTA III", "Elite"]
    },
    {
        "question": "Which game won the Best Indie Game award at The Game Awards 2023?",
        "answer": "Hades II",
        "options": ["Hades II", "Stray", "Cult of the Lamb", "Neon White"]
    },
    {
        "question": "Who is the developer behind the 'Elder Scrolls' series?",
        "answer": "Bethesda Game Studios",
        "options": ["Bethesda Game Studios", "FromSoftware", "Obsidian Entertainment", "CD Projekt Red"]
    },
    {
        "question": "Which game is regarded as the best vintage game from the 1980s?",
        "answer": "Pac-Man",
        "options": ["Pac-Man", "Donkey Kong", "Space Invaders", "Tetris"]
    },
    {
        "question": "Which game won the Best Game Direction award at The Game Awards 2023?",
        "answer": "Alan Wake II",
        "options": ["Alan Wake II", "Baldur's Gate III", "Spider-Man 2", "Starfield"]
    },
    {
        "question": "Which company developed 'Minecraft'?",
        "answer": "Mojang Studios",
        "options": ["Mojang Studios", "Microsoft", "Epic Games", "Valve"]
    },
    {
        "question": "Which game was the best-selling video game of all time as of 2023?",
        "answer": "Minecraft",
        "options": ["Minecraft", "GTA V", "Tetris", "Call of Duty: Modern Warfare"]
    },
    {
        "question": "Which game won the Best Narrative award at The Game Awards 2022?",
        "answer": "God of War Ragnarök",
        "options": ["God of War Ragnarök", "Elden Ring", "Stray", "Horizon Forbidden West"]
    },
    {
        "question": "Which company developed the game 'Cyberpunk 2077'?",
        "answer": "CD Projekt Red",
        "options": ["CD Projekt Red", "Naughty Dog", "Rockstar Games", "Bethesda"]
    },
    {
        "question": "Which game is known as one of the first open-world RPGs?",
        "answer": "The Elder Scrolls II: Daggerfall",
        "options": ["The Elder Scrolls II: Daggerfall", "The Legend of Zelda", "Final Fantasy VII", "Diablo II"]
    }
]

# === New: Define Tie-Breaker Questions with Multiple-Choice Options (15 questions) ===
tie_breaker_questions = [
    {
        "question": "Which developer is responsible for creating the 'Half-Life' series?",
        "answer": "Valve",
        "options": ["Valve", "Bethesda", "CD Projekt Red", "Epic Games"]
    },
    {
        "question": "What game won the Best Audio Design award at The Game Awards 2023?",
        "answer": "Elden Ring",
        "options": ["Elden Ring", "Baldur's Gate III", "The Legend of Zelda: Tears of the Kingdom", "Starfield"]
    },
    {
        "question": "Which company developed the game 'Hollow Knight'?",
        "answer": "Team Cherry",
        "options": ["Team Cherry", "Supergiant Games", "ConcernedApe", "Playdead"]
    },
    {
        "question": "What is the best-selling game console of all time as of 2023?",
        "answer": "PlayStation 2",
        "options": ["PlayStation 2", "Nintendo DS", "Xbox 360", "PlayStation 4"]
    },
    {
        "question": "Which game is known for introducing the Battle Royale genre?",
        "answer": "PlayerUnknown's Battlegrounds (PUBG)",
        "options": ["PlayerUnknown's Battlegrounds (PUBG)", "Fortnite", "Apex Legends", "Call of Duty: Warzone"]
    },
    {
        "question": "Who developed the game 'Celeste'?",
        "answer": "Matt Makes Games",
        "options": ["Matt Makes Games", "Supergiant Games", "Team Meat", "Dead Mage"]
    },
    {
        "question": "Which game won the Best Art Direction award at The Game Awards 2022?",
        "answer": "God of War Ragnarök",
        "options": ["God of War Ragnarök", "Elden Ring", "Stray", "Horizon Forbidden West"]
    },
    {
        "question": "What is the highest-grossing video game of all time as of 2023?",
        "answer": "Fortnite",
        "options": ["Fortnite", "Minecraft", "Grand Theft Auto V", "League of Legends"]
    },
    {
        "question": "Which game is considered a pioneer in the stealth genre?",
        "answer": "Metal Gear Solid",
        "options": ["Metal Gear Solid", "Splinter Cell", "Assassin's Creed", "Hitman"]
    },
    {
        "question": "Which company developed the game 'Horizon Zero Dawn'?",
        "answer": "Guerrilla Games",
        "options": ["Guerrilla Games", "CD Projekt Red", "FromSoftware", "Rockstar Games"]
    },
    {
        "question": "Which game won the Best Mobile Game award at The Game Awards 2023?",
        "answer": "League of Legends: Wild Rift",
        "options": ["League of Legends: Wild Rift", "Genshin Impact", "Among Us", "Clash Royale"]
    },
    {
        "question": "Which game is known for its unique blend of puzzle-solving and narrative storytelling developed by Thatgamecompany?",
        "answer": "Journey",
        "options": ["Journey", "Flower", "Sky: Children of the Light", "Gris"]
    },
    {
        "question": "Which game won the Best Performance award at The Game Awards 2023?",
        "answer": "Troy Baker as Joel in The Last of Us Part II",
        "options": [
            "Troy Baker as Joel in The Last of Us Part II",
            "Jennifer Hale as Commander Shepard in Mass Effect",
            "Ashley Johnson as Ellie in The Last of Us Part II",
            "Roger Clark as Jack in Death Stranding"
        ]
    },
    {
        "question": "Which company developed the game 'Ori and the Will of the Wisps'?",
        "answer": "Moon Studios",
        "options": ["Moon Studios", "Supergiant Games", "Playdead", "Team Cherry"]
    },
    {
        "question": "Which game is known for its procedurally generated worlds and permadeath mechanics, developed by Tynan Sylvester?",
        "answer": "Dead Cells",
        "options": ["Dead Cells", "Hades", "Spelunky", "Risk of Rain"]
    }
]

# Initialize session state
if 'group_scores' not in st.session_state:
    st.session_state.group_scores = {i: 0 for i in range(1, 11) if i != 5}  # Initialize scores for groups 1-10, skipping group 5
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'current_group' not in st.session_state:
    st.session_state.current_group = 1
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'used_questions' not in st.session_state:
    st.session_state.used_questions = []
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0  # Initialize question count

# === New: Initialize Tie-Breaker Session States ===
if 'is_tie_breaker' not in st.session_state:
    st.session_state.is_tie_breaker = False
if 'tie_breaker_groups' not in st.session_state:
    st.session_state.tie_breaker_groups = []
if 'tie_breaker_scores' not in st.session_state:
    st.session_state.tie_breaker_scores = {}
if 'tie_breaker_used_questions' not in st.session_state:
    st.session_state.tie_breaker_used_questions = []
if 'current_tie_breaker_group' not in st.session_state:
    st.session_state.current_tie_breaker_group = None
if 'tie_breaker_question' not in st.session_state:
    st.session_state.tie_breaker_question = None

# Function to get a new question (random 10 out of 25)
def get_new_question():
    if st.session_state.round == 1:
        available_questions = [q for q in questions_round_1 if q not in st.session_state.used_questions]
    elif st.session_state.round == 2:
        available_questions = [q for q in questions_round_2 if q not in st.session_state.used_questions]
    else:
        available_questions = []

    if available_questions and st.session_state.question_count < 10:
        question = random.choice(available_questions)
        st.session_state.used_questions.append(question)
        st.session_state.question_count += 1  # Increment question count

        if st.session_state.round == 2:
            # Shuffle the options to randomize their order
            shuffled_options = question["options"].copy()
            random.shuffle(shuffled_options)
            return {
                "question": question["question"],
                "options": shuffled_options,
                "answer": question["answer"]
            }
        else:
            return question
    return None

# === New: Function to get a new tie-breaker question ===
def get_new_tie_breaker_question():
    available_questions = [q for q in tie_breaker_questions if q not in st.session_state.tie_breaker_used_questions]

    if available_questions:
        question = random.choice(available_questions)
        st.session_state.tie_breaker_used_questions.append(question)
        # Shuffle the options to randomize their order
        shuffled_options = question["options"].copy()
        random.shuffle(shuffled_options)
        return {
            "question": question["question"],
            "options": shuffled_options,
            "answer": question["answer"]
        }
    return None

# === New: Add "options" to tie_breaker_questions ===
# Ensure that each tie-breaker question has an "options" key
for qb in tie_breaker_questions:
    if "options" not in qb:
        # If options are not defined, generate dummy options (you should replace these with accurate options)
        qb["options"] = [
            qb["answer"],
            "Option A",
            "Option B",
            "Option C"
        ]

# Container for main content to apply slight background for readability
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Display title and current group/round or Tie-Breaker
    st.markdown('<div class="title">GAMEHOLICS QUIZ</div>', unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>This is a quiz game about some of the most iconic and fan-favorite games!</div>",
                unsafe_allow_html=True)

    if not st.session_state.is_tie_breaker:
        st.markdown(
            f"<div class='group-score'>Group: {st.session_state.current_group} - Round: {st.session_state.round}</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div class='group-score'>Tie-Breaker Round - Group: {st.session_state.current_tie_breaker_group}</div>",
            unsafe_allow_html=True)

    # Get the current question
    if not st.session_state.is_tie_breaker:
        if st.session_state.current_question is None:
            st.session_state.current_question = get_new_question()
    else:
        if st.session_state.tie_breaker_question is None and st.session_state.tie_breaker_groups:
            st.session_state.current_tie_breaker_group = st.session_state.tie_breaker_groups.pop(0)
            st.session_state.tie_breaker_question = get_new_tie_breaker_question()

    # Calculate progress based on the question count
    if not st.session_state.is_tie_breaker:
        current_question_number = st.session_state.question_count
        total_questions = 10  # Total questions in a round

        # Adjust the total questions to reflect the number of active groups (excluding Group 5)
        active_groups = 9  # Groups 1-10 excluding Group 5
        progress_percentage = min(current_question_number / active_groups, 1.0)

        # Display progress label with adjusted numbering
        displayed_question_number = st.session_state.question_count
        st.markdown(f"<div class='progress-label'>Question {displayed_question_number} of {active_groups}</div>",
                    unsafe_allow_html=True)

        # Display progress bar inside a container at the bottom
        st.markdown("<div class='progress-container'>", unsafe_allow_html=True)
        st.progress(progress_percentage)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        # === New: Tie-Breaker Progress Display ===
        if st.session_state.current_tie_breaker_group:
            st.markdown(
                f"<div class='progress-label'>Tie-Breaker Question for Group {st.session_state.current_tie_breaker_group}</div>",
                unsafe_allow_html=True)
            st.markdown("<div class='progress-container'>", unsafe_allow_html=True)
            st.progress(0.1)  # Simple progress for tie-breaker
            st.markdown("</div>", unsafe_allow_html=True)

    # Display current question
    if not st.session_state.is_tie_breaker:
        if st.session_state.current_question:
            st.markdown(f"<div class='question'>{st.session_state.current_question['question']}</div>",
                        unsafe_allow_html=True)

            # Check if it's round 2 and display options as radio buttons
            if st.session_state.round == 2:
                options = st.session_state.current_question.get("options", [])
                if options:
                    selected_option = st.radio("Choose the correct answer:", options, key="round2_radio")

                    # Check answer when the user submits
                    if st.button("Submit Answer"):
                        if selected_option.strip().lower() == st.session_state.current_question["answer"].strip().lower():
                            st.session_state.group_scores[st.session_state.current_group] += 1
                            st.success("Correct answer! 🎉", icon="✅")
                        else:
                            st.error("Wrong answer!", icon="❌")
                        st.markdown(f"<div class='answer'>Correct Answer: {st.session_state.current_question['answer']}</div>",
                                    unsafe_allow_html=True)
                        st.session_state.answered = True
                else:
                    st.error("No options available for this question.", icon="🚫")
            else:
                # Input for the answer in round 1
                answer = st.text_input("Your Answer:", "", key="answer_input")

                # Check answer when the user submits
                if st.button("Submit Answer"):
                    if answer.strip().lower() == st.session_state.current_question["answer"].strip().lower():
                        st.session_state.group_scores[st.session_state.current_group] += 1
                        st.success("Correct answer! 🎉", icon="✅")
                    else:
                        st.error("Wrong answer!", icon="❌")
                    st.markdown(f"<div class='answer'>Correct Answer: {st.session_state.current_question['answer']}</div>",
                                unsafe_allow_html=True)
                    st.session_state.answered = True
    else:
        if st.session_state.tie_breaker_question:
            st.markdown(f"<div class='question'>{st.session_state.tie_breaker_question['question']}</div>",
                        unsafe_allow_html=True)

            # Display options as radio buttons for Tie-Breaker
            options = st.session_state.tie_breaker_question.get("options", [])
            if options:
                selected_tie_option = st.radio("Choose the correct answer:", options, key="tie_breaker_radio")

                # Check answer when the user submits
                if st.button("Submit Tie-Breaker Answer"):
                    if selected_tie_option.strip().lower() == st.session_state.tie_breaker_question["answer"].strip().lower():
                        st.session_state.tie_breaker_scores[
                            st.session_state.current_tie_breaker_group] = st.session_state.tie_breaker_scores.get(
                            st.session_state.current_tie_breaker_group, 0) + 1
                        st.success(f"Correct answer for Group {st.session_state.current_tie_breaker_group}! 🎉", icon="✅")
                    else:
                        st.error(f"Wrong answer for Group {st.session_state.current_tie_breaker_group}!", icon="❌")
                    st.markdown(
                        f"<div class='answer'>Correct Answer: {st.session_state.tie_breaker_question['answer']}</div>",
                        unsafe_allow_html=True)
                    st.session_state.answered = True
            else:
                st.error("No options available for this tie-breaker question.", icon="🚫")

    # Button to get a new question for the next group or next tie-breaker
    if (not st.session_state.is_tie_breaker and st.session_state.answered) or \
            (
                    st.session_state.is_tie_breaker and st.session_state.answered and st.session_state.current_tie_breaker_group):
        if not st.session_state.is_tie_breaker:
            if st.button("Next Group"):
                st.session_state.current_group += 1
                if st.session_state.current_group == 5:  # Skip Group 5
                    st.session_state.current_group += 1
                if st.session_state.current_group > 10:  # Reset to Group 1
                    st.session_state.current_group = 1

                    if st.session_state.round == 1:
                        st.session_state.round += 1
                        st.session_state.used_questions = []
                        st.session_state.question_count = 0  # Reset for Round 2
                        st.success("Round 1 complete! Starting Round 2.")
                        st.session_state.current_question = get_new_question()
                        st.session_state.answered = False
                    else:
                        # All rounds complete, show final scores
                        st.success("Final Scores:")
                        st.markdown('<div class="final-score-box">', unsafe_allow_html=True)
                        for group, score in st.session_state.group_scores.items():
                            st.markdown(f"<div class='final-score'>{group}: {score} points</div>",
                                        unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                        max_score = max(st.session_state.group_scores.values())

                        if max_score > 0:
                            winners = [group for group, score in st.session_state.group_scores.items() if
                                       score == max_score]

                            if len(winners) > 1:
                                # === New: Initiate Tie-Breaker ===
                                st.warning("There's a tie! Initiating Tie-Breaker Round.", icon="⚠️")

                                st.session_state.is_tie_breaker = True
                                st.session_state.tie_breaker_groups = winners.copy()
                                st.session_state.tie_breaker_scores = {group: 0 for group in winners}
                                st.session_state.current_tie_breaker_group = None
                                st.session_state.tie_breaker_question = None
                                st.session_state.tie_breaker_used_questions = []
                                st.session_state.answered = False
                            else:
                                # === Existing: Declare Winner ===
                                if max_score > 0:
                                    st.markdown(
                                        f"<div class='winner'>🎉 Winner: Group {winners[0]} with {max_score} points! 🎉</div>",
                                        unsafe_allow_html=True)
                                else:
                                    st.markdown(f"<div class='winner'>😞 No one wins.</div>",
                                                unsafe_allow_html=True)
                        else:
                            st.markdown(f"<div class='winner'>😞 No one wins.</div>",
                                        unsafe_allow_html=True)

                else:
                    # Move to the next question and reset the "answered" state
                    st.session_state.current_question = get_new_question()
                    st.session_state.answered = False
        else:
            if st.button("Next Tie-Breaker Question"):
                st.session_state.current_tie_breaker_group = None
                st.session_state.tie_breaker_question = None
                st.session_state.answered = False

    # After all tie-breaker questions have been asked
    if st.session_state.is_tie_breaker and not st.session_state.tie_breaker_groups and not st.session_state.current_tie_breaker_group and not st.session_state.tie_breaker_question:
        # Determine the winner based on tie-breaker scores
        st.success("Tie-Breaker Rounds Complete!")
        st.markdown("Final Tie-Breaker Scores:")
        st.markdown('<div class="final-score-box">', unsafe_allow_html=True)
        for group, score in st.session_state.tie_breaker_scores.items():
            st.markdown(f"<div class='final-score'>{group}: {score} points</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        max_tie_score = max(st.session_state.tie_breaker_scores.values())
        final_winners = [group for group, score in st.session_state.tie_breaker_scores.items() if
                         score == max_tie_score and score > 0]

        if len(final_winners) > 1:
            winner_text = ", ".join([f"Group {group}" for group in final_winners])
            st.markdown(
                f"<div class='winner'>🎉 Tie-Breaker Winners: {winner_text} with {max_tie_score} points! 🎉</div>",
                unsafe_allow_html=True)
        elif len(final_winners) == 1:
            st.markdown(
                f"<div class='winner'>🎉 Tie-Breaker Winner: Group {final_winners[0]} with {max_tie_score} points! 🎉</div>",
                unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='winner'>😞 No one wins in the Tie-Breaker, let the host decide.</div>",
                        unsafe_allow_html=True)

        # Reset tie-breaker state to prevent re-execution
        st.session_state.is_tie_breaker = False
        st.session_state.tie_breaker_groups = []
        st.session_state.tie_breaker_scores = {}
        st.session_state.tie_breaker_used_questions = []
        st.session_state.current_tie_breaker_group = None
        st.session_state.tie_breaker_question = None

    st.markdown('</div>', unsafe_allow_html=True)
