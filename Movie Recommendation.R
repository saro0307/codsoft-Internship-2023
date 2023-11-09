# Install and load necessary packages
if (!require("tm")) install.packages("tm", dependencies=TRUE)
if (! require("proxy")) install.packages("proxy", dependencies=TRUE)
library(tm)
library(proxy)

# Real dataset of movies
movies <- data.frame(
  Title = c("The Shawshank Redemption", "The Godfather", "Pulp Fiction", "The Dark Knight", "Schindler's List"),
  Description = c(
    "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    "When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
    "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis."
  )
)

# Create a corpus
corpus <- Corpus(VectorSource(movies$Description))

# Create a document-term matrix (DTM)
dtm <- DocumentTermMatrix(corpus)

# Compute cosine similarity between movie descriptions
similarity_matrix <- proxy::simil(as.matrix(dtm), method = "cosine")

# Function to get movie recommendations
get_recommendations <- function(title) {
  idx <- which(movies$Title == title)
  sim_scores <- as.matrix(similarity_matrix)[idx, ]
  sim_scores <- sort(sim_scores, decreasing = TRUE)
  top_similar_movies <- movies$Title[head(order(sim_scores), 4)[-1]]
  return(top_similar_movies)
}

# Example usage:
user_preference <- "The Shawshank Redemption"
recommendations <- get_recommendations(user_preference)
cat("Recommended movies for", user_preference, ":\n", recommendations, "\n")
