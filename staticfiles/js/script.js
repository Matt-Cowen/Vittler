document.addEventListener("DOMContentLoaded", () => {
            const recipeForm = document.getElementById("recipeForm");
            const submitButton = document.getElementById("submitButton");
            const editButtons = document.getElementsByClassName("btn-edit");

            /*
             * Initializes edit functionality for the provided edit buttons.
             * 
             * For each button in the `editButtons` collection:
             * - Retrieves the associated comment's ID upon click.
             * - Fetches the content of the corresponding comment.
             * - Populates the `commentText` input/textarea with the comment's content for editing.
             * - Updates the submit button's text to "Update".
             * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
             */

            for (let button of submitButtons) {
                button.addEventListener("click", (e) => {
                    recipeForm.setAttribute("action");
                });
            }

            // for (let button of editButtons) {
            //     button.addEventListener("click", (e) => {
            //         let recipeId = e.target.getAttribute("recipe_id");
            //         recipeForm.action = `/submit_recipe/`;
            //         recipeTitle.value = recipeTitle;
            //         submitButton.innerText = "Update";
            //     });
            // }
            // })


            for (let button of editButtons) {
                button.addEventListener("click", (e) => {
                    const recipeId = e.target.getAttribute("recipe_id");
                    const recipeTitle = document.getElementById(`${recipeId}-card-title-id`).innerText;

                    console.log(`${recipeId}-card-title-id`);

                    // Update the form's action URL dynamically
                    recipeForm.action = `/submit_recipe/`;

                    // Pre-fill the form fields (you may need to fetch recipe details via AJAX for full details)
                    document.getElementById("id_title").value = recipeTitle;

                    // Update the button text
                    submitButton.innerText = "Update Recipe";

                    // Optionally scroll to the form or display it dynamically
                    recipeForm.scrollIntoView({
                        behavior: "smooth"
                    });
                });
            };
        });