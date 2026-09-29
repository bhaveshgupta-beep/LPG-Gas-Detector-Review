const ratingSlider = document.getElementById("rating");
const ratingValue = document.getElementById("ratingValue");
const ratingMessage = document.getElementById("ratingMessage");
const stars = document.getElementById("stars");
const hiddenRating = document.getElementById("hiddenRating");

function updateRating() {

    const rating = Number(ratingSlider.value);

    ratingValue.textContent = rating;

    hiddenRating.value = rating;

    stars.textContent =
        "★".repeat(rating) +
        "☆".repeat(5 - rating);

    if (rating <= 2) {

        ratingMessage.textContent =
            "Was it that bad? I'm sorry to hear that 😭 I'll do it better next time.";

    } else if (rating === 3) {

        ratingMessage.textContent =
            "Thanks for the review, I really appreciate it! 💙";

    } else if (rating === 4) {

        ratingMessage.textContent =
            "Thankkk youuuu sooo muchhhh 🥹💙 I really appreciate it!";

    } else {

        ratingMessage.textContent =
            "Thank you so much! Your review gives us relief that solving those errors was worth it 🥹💙✨🫶";
    }

    const percentage = ((rating - 1) / 4) * 100;

    ratingSlider.style.background =
        `linear-gradient(
            to right,
            #00eaff ${percentage}%,
            rgba(255,255,255,0.12) ${percentage}%
        )`;
}

ratingSlider.addEventListener("input", updateRating);

updateRating();