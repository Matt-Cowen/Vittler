//Variables

const editButtons = document.getElementsByClassName("btn-edit");
const deleteButtons = document.getElementsByClassName("btn-delete");
const preDeleteButtons = document.getElementsByClassName("btn-predelete");
const cancelButtons = document.getElementsByClassName("btn-cancel");

//Message display timeout

document.addEventListener("DOMContentLoaded", function() {
    const messages = document.getElementById("message-display");
    if (messages) {
      setTimeout(() => {
        messages.style.display = "none";
      }, 5000); 
    }
  });

//Edit to adapt display of modal and render populated Recipe Edit form

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
}


//Button to adapt modal display to show delete confirmation

for (let button of preDeleteButtons) {
  button.addEventListener("click", (e) => {
    let recipeId = e.target.getAttribute("data-recipe_id");
    let recipeModal = document.getElementById(`${recipeId}-modal-content`);
    let editModal = document.getElementById(`${recipeId}-modal-edit`);
    let recipeEditButton = document.getElementById(`${recipeId}-edit-button`);
    let recipeAddButton = document.getElementById(`${recipeId}-add-button`);
    let recipeDeleteConfirm = document.getElementById(`${recipeId}-modal-delete`);
    let preDeleteButton = document.getElementById(`${recipeId}-predelete-button`);

    //Toggle modal view
    editModal.classList.add("d-none");
    recipeModal.classList.add("d-none");
    recipeAddButton.classList.add("d-none");
    recipeEditButton.classList.add("d-none");
    recipeDeleteConfirm.classList.remove("d-none");
    preDeleteButton.classList.add("d-none");
  });
}


//Button functionality to delete recipe

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let deleteUrl = e.target.getAttribute("data-url");
          
        window.location.href = deleteUrl;

    });
}

//Button functionality to cancel delete recipe

for (let button of cancelButtons) {
  button.addEventListener("click", (e) => {
    let libraryUrl = e.target.getAttribute("data-url");
    window.location.href = libraryUrl + '?refresh=true';  //Refresh page to remove classes added by predelete
  });
}

//Button functionality to clear search parameters

function clearSearch() {
  let libraryUrl = ("data-url");
  window.location.href = libraryUrl;
}
