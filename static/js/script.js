document.addEventListener("DOMContentLoaded", () => {

            const submitButton = document.getElementById("submitButton");
            const editButtons = document.getElementsByClassName("btn-edit");
            const titleText = document.getElementById("id_title");
            const deleteButtons = document.getElementsByClassName("btn-delete");

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
                    
                    
                    let recipeId = e.target.getAttribute("data-recipe_id");
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
            
            // for (let button of deleteButtons) {
            //     button.addEventListener("click", (e) => {
            //         let recipeId = e.target.getAttribute("data-recipe_id");
            //         deleteButtons.href = `library/recipe_delete/${recipeId}`
            //     })
            // }

            for (let button of deleteButtons) {
                button.addEventListener("click", (e) => {
                    e.preventDefault(); // Prevent default link action
                    let deleteUrl = e.target.getAttribute("data-url")
                    if (confirm("Are you sure you want to delete this recipe?")) {
                        // Redirect to delete URL
                        window.location.href = deleteUrl;
                    }
                });
            }

        });