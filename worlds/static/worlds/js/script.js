// Lorekeeper JavaScript

document.addEventListener("DOMContentLoaded", function () {
    const collapsibleButtons = document.querySelectorAll(".collapsible-toggle");

    collapsibleButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const targetId = button.getAttribute("data-target");
            const targetContent = document.getElementById(targetId);

            if (!targetContent) {
                return;
            }

            const isExpanded = button.getAttribute("aria-expanded") === "true";

            button.setAttribute("aria-expanded", String(!isExpanded));
            targetContent.classList.toggle("collapsed-section");

            if (isExpanded) {
                button.textContent = "Show";
            } else {
                button.textContent = "Hide";
            }
        });
    });
});