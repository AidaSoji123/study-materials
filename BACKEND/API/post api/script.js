async function searchPostOffices() {
        const pinCode = document.getElementById('pinCodeInput').value.trim();
    const apiUrl = `https://api.postalpincode.in/pincode/${pinCode}`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        displayPostOffices(data);
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('resultContainer').innerHTML = 'Error fetching data';
    }
}

function displayPostOffices(data) {
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.innerHTML = ''; // Clear previous results

    if (data && data.length > 0 && data[0].Status === 'Success') {
        const postOffices = data[0].PostOffice;
        if (postOffices && postOffices.length > 0) {
            const ul = document.createElement('ul');
            postOffices.forEach(postOffice => {
                const li = document.createElement('li');
                li.textContent = `${postOffice.Name}, ${postOffice.District}, ${postOffice.State}`;
                ul.appendChild(li);
            });
            resultContainer.appendChild(ul);
        } else {
            resultContainer.textContent = 'No post offices found for this pin code.';
        }
    } else {
        resultContainer.textContent = 'Invalid pin code or no data available.';
    }
}
