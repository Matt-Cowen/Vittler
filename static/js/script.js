document.addEventListener("DOMContentLoaded", () => {
            const recipeForm = document.getElementById("recipeForm");
            const submitButton = document.getElementById("submitButton");
            const editButtons = document.getElementsByClassName("btn-edit");
            const titleText = document.getElementById("id_title");

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

            // for (let button of submitButtons) {
            //     button.addEventListener("click", (e) => {
            //         recipeForm.setAttribute("action");
            //     });
            // }

            for (let button of editButtons) {
                button.addEventListener("click", (e) => {
                    let recipeId = e.target.getAttribute("recipe_id");
                    let recipeTitle = document.getElementById(`${recipeId}-card-title-id`).innerText;

                    window.location.href = `/edit_recipe/${recipeId}`


                    console.log(recipeTitle);                    
                    titleText.value = recipeTitle;
                    submitButton.innerText = "Update";
                    recipeForm.setAttribute("action", `edit_recipe/${recipeId}`);
                });
            };

        });