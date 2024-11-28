document.addEventListener("DOMContentLoaded", () => {

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
                    let editModal = document.getElementById(`${recipeId}-modal-edit`);
                    let recipeTitle = document.getElementById(`${recipeId}-card-title-id`).innerText;
                    let recipeForm = document.getElementById(`${recipeId}-modal-edit-form`);

                    //Toggle modal view
                    editModal.classList.toggle("d-none")

                    console.log(recipeTitle);
                    console.log(recipeId); 

                    recipeForm.setAttribute("action", `edit_recipe/${recipeId}/`);
                });
            };

        });