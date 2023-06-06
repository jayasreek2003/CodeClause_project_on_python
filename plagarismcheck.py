import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Join the tokens back into a single string
    processed_text = ' '.join(tokens)
    
    return processed_text

def calculate_similarity(text1, text2):
    # Preprocess the texts
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the preprocessed texts
    tfidf_matrix = vectorizer.fit_transform([processed_text1, processed_text2])

    # Calculate the cosine similarity
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    return similarity_score

def check_plagiarism(text1, text2, threshold=0.8):
    similarity_score = calculate_similarity(text1, text2)

    if similarity_score >= threshold:
        print("Plagiarism detected!")
    else:
        print("No plagiarism detected.")

# Example usage
text1 = "This is the original text."
text2 = "This is some plagiarized text."

check_plagiarism(text1, text2)
