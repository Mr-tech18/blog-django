export function filtering(checkboxClassName,formId,containerId){
    let selected_data = {};
    document.querySelectorAll(checkboxClassName).forEach((item, index) => {
        item.addEventListener('click', () => {
            let data_key = item.dataset.filter;

            selected_data[data_key] = Array.from(
                document.querySelectorAll('[data-filter=' + data_key + ']:checked')
            ).map(element => element.value);
            
           

            // Convert selected_data to URL parameters
            let params = new URLSearchParams();
            Object.keys(selected_data).forEach(key => {
                selected_data[key].forEach(value => params.append(`${key}[]`, value));
            });
            console.log(selected_data);
            let xhr = new XMLHttpRequest();
            xhr.open('GET', `${document.getElementById(formId).getAttribute('action')}?${params.toString()}`, true);
            xhr.setRequestHeader('Content-type', 'application/json');

            xhr.onreadystatechange = function() {
                if (this.readyState === 3) {
                    
                }
                if (this.readyState === 4 && (this.status >= 200 && this.status < 204)) {
                    let data = JSON.parse(this.responseText);
                    let postContainer = document.getElementById(containerId);
                    postContainer.innerHTML = data.context;
                }
            };
            xhr.onerror = function() {
                console.log('Error...');
            };
            xhr.send(); // No data in the send method for GET request
        });
    });
}

    
    

document.addEventListener('DOMContentLoaded', () => {
    // Function for post filtering
    filtering('.checkbox-filter','my_form','post_container');
});
