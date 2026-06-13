// Lorekeeper frontend JavaScript

document.addEventListener("DOMContentLoaded", function () {
    initialiseCollapsibleSections();
    initialiseWorldFormPreview();
});


function initialiseCollapsibleSections() {
    /*
     * Allows users to show and hide content sections on detail pages.
     * This is used on world, character and lore entry detail pages.
     */

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
}


function initialiseWorldFormPreview() {
    /*
     * Updates the live preview card on the create/edit world form.
     * If the preview card is not on the current page, the function stops.
     */

    const previewCard = document.getElementById("world-preview-card");

    if (!previewCard) {
        return;
    }

    // Get the Django form fields by their automatically generated IDs.
    const titleInput = document.getElementById("id_title");
    const genreInput = document.getElementById("id_genre");
    const summaryInput = document.getElementById("id_summary");
    const conflictInput = document.getElementById("id_main_conflict");
    const toneInput = document.getElementById("id_tone");
    const publicInput = document.getElementById("id_is_public");

    // Get the preview elements that will be updated as the user types.
    const previewTitle = document.getElementById("preview-title");
    const previewGenre = document.getElementById("preview-genre");
    const previewVisibility = document.getElementById("preview-visibility");
    const previewSummary = document.getElementById("preview-summary");
    const previewConflict = document.getElementById("preview-conflict");
    const previewTone = document.getElementById("preview-tone");

    function updatePreview() {
        /*
         * Copies the current form values into the preview card.
         * Placeholder text is shown when fields are empty.
         */

        previewTitle.textContent = titleInput.value.trim() || "Untitled World";

        if (genreInput.selectedIndex >= 0) {
            previewGenre.textContent = genreInput.options[genreInput.selectedIndex].text;
        } else {
            previewGenre.textContent = "Genre not selected";
        }

        previewSummary.textContent = (
            summaryInput.value.trim() || "Your world summary will appear here."
        );

        previewConflict.textContent = (
            conflictInput.value.trim() || "Main conflict will appear here if added."
        );

        previewTone.textContent = (
            toneInput.value.trim() || "Tone will appear here if added."
        );

        if (publicInput.checked) {
            previewVisibility.textContent = "Public";
            previewVisibility.classList.remove("badge-private");
            previewVisibility.classList.add("badge-public");
        } else {
            previewVisibility.textContent = "Private";
            previewVisibility.classList.remove("badge-public");
            previewVisibility.classList.add("badge-private");
        }
    }

    const formInputs = [
        titleInput,
        genreInput,
        summaryInput,
        conflictInput,
        toneInput,
        publicInput
    ];

    formInputs.forEach(function (input) {
        if (input) {
            input.addEventListener("input", updatePreview);
            input.addEventListener("change", updatePreview);
        }
    });

    updatePreview();
}