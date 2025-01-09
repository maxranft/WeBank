// scripts.js

document.addEventListener("DOMContentLoaded", () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", event => {
            const targetId = event.target.getAttribute("href");
            if (targetId.startsWith("#")) {
                event.preventDefault();
                document.querySelector(targetId)?.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    // Interactive hover effects for feature cards
    const featureCards = document.querySelectorAll(".feature");
    featureCards.forEach(card => {
        card.addEventListener("mouseover", () => {
            card.style.transform = "scale(1.05)";
            card.style.boxShadow = "0 8px 15px rgba(0, 0, 0, 0.2)";
            card.style.transition = "transform 0.3s, box-shadow 0.3s";
        });
        card.addEventListener("mouseout", () => {
            card.style.transform = "scale(1)";
            card.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)";
        });
    });

    // Dynamic year update in footer
    const footerYear = document.querySelector("footer p");
    if (footerYear) {
        const currentYear = new Date().getFullYear();
        footerYear.textContent = `© ${currentYear} WeBank. All rights reserved.`;
    }

    // Placeholder functionality for "Get Started" button
    const getStartedButton = document.querySelector(".btn-primary");
    if (getStartedButton) {
        getStartedButton.addEventListener("click", event => {
            event.preventDefault();
            alert("Feature coming soon! Stay tuned.");
        });
    }

    // Scroll-to-top button
    const scrollToTopButton = document.createElement("button");
    scrollToTopButton.textContent = "↑";
    scrollToTopButton.style.position = "fixed";
    scrollToTopButton.style.bottom = "20px";
    scrollToTopButton.style.right = "20px";
    scrollToTopButton.style.display = "none";
    scrollToTopButton.style.padding = "10px";
    scrollToTopButton.style.border = "none";
    scrollToTopButton.style.borderRadius = "50%";
    scrollToTopButton.style.backgroundColor = "#2b6cb0";
    scrollToTopButton.style.color = "white";
    scrollToTopButton.style.cursor = "pointer";
    scrollToTopButton.style.zIndex = "1000";
    document.body.appendChild(scrollToTopButton);

    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            scrollToTopButton.style.display = "block";
        } else {
            scrollToTopButton.style.display = "none";
        }
    });

    scrollToTopButton.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    // Navbar shrink on scroll
    const navbar = document.querySelector(".navbar");
    if (navbar) {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 50) {
                navbar.style.backgroundColor = "#1e4f7a";
                navbar.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)";
            } else {
                navbar.style.backgroundColor = "#2b6cb0";
                navbar.style.boxShadow = "none";
            }
        });
    }

    // Real-time cryptocurrency price placeholder functionality
    const livePricesLink = document.querySelector("a[href='#live-prices']");
    if (livePricesLink) {
        livePricesLink.addEventListener("click", event => {
            event.preventDefault();
            alert("Live cryptocurrency prices will be available soon!");
        });
    }
});
