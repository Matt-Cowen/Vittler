document.addEventListener("DOMContentLoaded", function() {
    const messages = document.getElementById("message-display");
    if (messages) {
      setTimeout(() => {
        messages.style.display = "none"; // Hide the messages
      }, 5000); // 5000 milliseconds = 5 seconds
    }
  });



const submitButton = document.getElementById("submitButton");
const editButtons = document.getElementsByClassName("btn-edit");
const titleText = document.getElementById("id_title");
const deleteButtons = document.getElementsByClassName("btn-delete");


for (let button of editButtons) {
    button.addEventListener("click", (e) => {


        let recipeId = e.target.getAttribute("data-recipe_id");
        let recipeModal = document.getElementById(`${recipeId}-modal-content`);
        let editModal = document.getElementById(`${recipeId}-modal-edit`);
        let recipeForm = document.getElementById(`${recipeId}-modal-edit-form`);

        //Toggle modal view
        editModal.classList.toggle("d-none")
        recipeModal.classList.toggle("d-none")


        recipeForm.setAttribute("action", `edit_recipe/${recipeId}/`);
    });
};


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

