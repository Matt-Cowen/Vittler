document.addEventListener("DOMContentLoaded", function() {
    const messages = document.getElementById("message-display");
    if (messages) {
      setTimeout(() => {
        messages.style.display = "none";
      }, 5000); 
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
        let recipeEditButton = document.getElementById(`${recipeId}-edit-button`);
        let recipeAddButton = document.getElementById(`${recipeId}-add-button`);

        //Toggle modal view
        editModal.classList.toggle("d-none");
        recipeModal.classList.toggle("d-none");
        recipeAddButton.classList.toggle("d-none");

        if (recipeEditButton.innerText.includes("Cancel")) {
          recipeEditButton.innerText = "Edit";
        } else {
          recipeEditButton.innerText = "Cancel Edit";
        }

        //Set submit action
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


function clearSearch() {
  let libraryUrl = e.target.getAttribute("data-url")
  window.location.href = libraryUrl;
}
