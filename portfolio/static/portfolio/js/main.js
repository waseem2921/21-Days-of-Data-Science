const root = document.documentElement;
const themeButton = document.getElementById("themeToggle");
const savedTheme = localStorage.getItem("portfolioTheme");

if (savedTheme) {
    root.setAttribute("data-theme", savedTheme);
}

if (themeButton) {
    themeButton.addEventListener("click", () => {
        const currentTheme = root.getAttribute("data-theme") || "light";
        const nextTheme = currentTheme === "light" ? "dark" : "light";
        root.setAttribute("data-theme", nextTheme);
        localStorage.setItem("portfolioTheme", nextTheme);
    });
}

const counters = document.querySelectorAll(".counter");
const observer = new IntersectionObserver(
    (entries, obs) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }
            const counter = entry.target;
            const target = parseInt(counter.dataset.target || "0", 10);
            let current = 0;
            const step = Math.max(1, Math.ceil(target / 45));

            const tick = () => {
                current += step;
                if (current >= target) {
                    counter.textContent = target;
                    return;
                }
                counter.textContent = current;
                requestAnimationFrame(tick);
            };

            requestAnimationFrame(tick);
            obs.unobserve(counter);
        });
    },
    { threshold: 0.4 }
);

counters.forEach((counter) => observer.observe(counter));
