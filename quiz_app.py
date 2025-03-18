import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="General Knowledge Quiz",
    page_icon="🧠",
    layout="centered"
)

# Define quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Pacific Ocean"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Oganesson"],
        "correct_answer": "Oxygen"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1943", "1945", "1947", "1950"],
        "correct_answer": "1945"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Won", "Yen", "Ringgit"],
        "correct_answer": "Yen"
    },
    {
        "question": "Which country is home to the Great Barrier Reef?",
        "options": ["Brazil", "Australia", "Thailand", "Mexico"],
        "correct_answer": "Australia"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "correct_answer": "2"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "correct_answer": "Albert Einstein"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["Banana", "Avocado", "Cucumber", "Spinach"],
        "correct_answer": "Avocado"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Thailand", "Japan", "South Korea"],
        "correct_answer": "Japan"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "correct_answer": "Diamond"
    },
    {
        "question": "Who was the first person to step on the moon?",
        "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "John Glenn"],
        "correct_answer": "Neil Armstrong"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Liver", "Brain", "Skin"],
        "correct_answer": "Skin"
    },
    {
        "question": "Which country gifted the Statue of Liberty to the United States?",
        "options": ["England", "France", "Spain", "Italy"],
        "correct_answer": "France"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "correct_answer": "Canberra"
    },
    {
        "question": "Which instrument has 88 keys?",
        "options": ["Guitar", "Violin", "Piano", "Flute"],
        "correct_answer": "Piano"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "correct_answer": "Au"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Mississippi", "Yangtze"],
        "correct_answer": "Nile"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
        "correct_answer": "Ottawa"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"],
        "correct_answer": "Alexander Graham Bell"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Gobi Desert", "Antarctic Desert", "Arabian Desert"],
        "correct_answer": "Antarctic Desert"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "correct_answer": "Saturn"
    },
    {
        "question": "What is the national animal of Australia?",
        "options": ["Koala", "Kangaroo", "Emu", "Platypus"],
        "correct_answer": "Kangaroo"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["J.K. Rowling", "Harper Lee", "Ernest Hemingway", "Mark Twain"],
        "correct_answer": "Harper Lee"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["90°C", "100°C", "110°C", "212°C"],
        "correct_answer": "100°C"
    },
    {
        "question": "Which famous ship sank on its maiden voyage in 1912?",
        "options": ["Lusitania", "Queen Mary", "Titanic", "Britannic"],
        "correct_answer": "Titanic"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
        "correct_answer": "Vatican City"
    },
    {
        "question": "Which vitamin is produced when your skin is exposed to sunlight?",
        "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"],
        "correct_answer": "Vitamin D"
    },
    {
        "question": "What is the main language spoken in Brazil?",
        "options": ["Spanish", "Portuguese", "English", "French"],
        "correct_answer": "Portuguese"
    },
    {
        "question": "Who is known as the father of modern physics?",
        "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei"],
        "correct_answer": "Albert Einstein"
    },
    {
        "question": "Which country is home to the Taj Mahal?",
        "options": ["Pakistan", "India", "Bangladesh", "Nepal"],
        "correct_answer": "India"
    }
]

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'questions' not in st.session_state:
    # Shuffle questions
    shuffled_questions = quiz_questions.copy()
    random.shuffle(shuffled_questions)
    st.session_state.questions = shuffled_questions
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = len(st.session_state.questions)
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# Function to handle next question
def next_question():
    st.session_state.show_result = False
    st.session_state.selected_option = None
    if st.session_state.current_question < st.session_state.total_questions - 1:
        st.session_state.current_question += 1
    else:
        st.session_state.quiz_completed = True

# Function to check answer
def check_answer(selected_option, correct_answer):
    st.session_state.selected_option = selected_option
    st.session_state.show_result = True
    if selected_option == correct_answer:
        st.session_state.score += 1

# Function to restart quiz
def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False
    st.session_state.show_result = False
    st.session_state.selected_option = None
    # Reshuffle questions
    shuffled_questions = quiz_questions.copy()
    random.shuffle(shuffled_questions)
    st.session_state.questions = shuffled_questions

# Main app
st.title("🧠 General Knowledge Quiz")
st.write("Test your knowledge with these general knowledge questions!")

# Progress bar
progress = st.session_state.current_question / st.session_state.total_questions
st.progress(progress)
st.write(f"Question {st.session_state.current_question + 1} of {st.session_state.total_questions}")

# Display current score
st.sidebar.header("Score")
st.sidebar.write(f"{st.session_state.score} / {st.session_state.total_questions}")

# Quiz completion screen
if st.session_state.quiz_completed:
    st.success(f"Quiz completed! Your final score is {st.session_state.score} out of {st.session_state.total_questions}.")
    
    # Calculate percentage
    percentage = (st.session_state.score / st.session_state.total_questions) * 100
    
    # Display different messages based on score
    if percentage >= 90:
        st.balloons()
        st.write("🏆 Outstanding! You're a general knowledge expert!")
    elif percentage >= 70:
        st.write("🎓 Great job! You have excellent general knowledge!")
    elif percentage >= 50:
        st.write("👍 Good effort! You know quite a bit!")
    else:
        st.write("📚 Keep learning! There's always room for improvement.")
    
    # Restart button
    if st.button("Restart Quiz"):
        restart_quiz()
        st.rerun()  # Changed from st.experimental_rerun()
else:
    # Display current question
    current_q = st.session_state.questions[st.session_state.current_question]
    st.subheader(current_q["question"])
    
    # Display options
    option_cols = st.columns(1)
    
    with option_cols[0]:
        for option in current_q["options"]:
            button_key = f"{current_q['question']}_{option}"
            
            # Use only supported button types
            button_type = "primary"
            
            # Disable buttons after selection
            button_disabled = st.session_state.show_result
            
            if st.button(option, key=button_key, type=button_type, disabled=button_disabled):
                check_answer(option, current_q["correct_answer"])
    
    # Show feedback after selection
    if st.session_state.show_result:
        if st.session_state.selected_option == current_q["correct_answer"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect! The correct answer is: {current_q['correct_answer']}")
        
        # Next question button
        if st.button("Next Question"):
            next_question()
            st.rerun()  # Changed from st.experimental_rerun()

# Add a footer
st.markdown("---")
st.markdown("Made by ❤️ Mussawir Sohail")