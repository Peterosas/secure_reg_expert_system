// Intersection Observer to detect when the form enters the viewport
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        // Check if the form section is in view
        if (entry.isIntersecting) {
            entry.target.classList.add('visible'); // Add the visible class to trigger animations
            observer.unobserve(entry.target); // Stop observing once the form is revealed
        }
    });
}, {
    threshold: 0.5, // Trigger the animation when 50% of the form is in view
});

// Start observing the form section
const formSection = document.querySelector('.signup-form-section');
observer.observe(formSection);
