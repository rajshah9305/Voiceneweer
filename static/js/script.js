// static/js/script.js

document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const button = form.querySelector('button');

    const statusContainer = document.getElementById('status-container');
    const statusMessage = document.getElementById('status-message');
    const resultContainer = document.getElementById('result-container');
    const resultAudio = document.getElementById('result-audio');
    const downloadLink = document.getElementById('download-link');

    // --- UI Update: Show loading state ---
    button.disabled = true;
    resultContainer.classList.add('hidden');
    statusContainer.classList.remove('hidden');
    statusMessage.textContent = 'Uploading and converting... Please wait.';
    statusMessage.style.color = '#333';

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            // If server returns an error (like 4xx or 5xx)
            throw new Error(data.detail || 'An unknown error occurred.');
        }

        // --- UI Update: Show success state ---
        statusContainer.classList.add('hidden');
        resultContainer.classList.remove('hidden');

        resultAudio.src = data.url;
        resultAudio.load(); // Prepares the audio player
        resultAudio.play();

        downloadLink.href = data.url;
        downloadLink.setAttribute('download', data.url.split('/').pop());

    } catch (error) {
        // --- UI Update: Show error state ---
        statusContainer.classList.remove('hidden');
        statusMessage.textContent = `Error: ${error.message}`;
        statusMessage.style.color = 'red';
        console.error('Conversion failed:', error);
    } finally {
        // --- UI Update: Re-enable form ---
        button.disabled = false;
        form.reset(); // Clear the form fields
    }
});

