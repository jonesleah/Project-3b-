document.getElementById('email-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const emailContent = document.getElementById('email-input').value;
    const response = await fetch('/api/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: emailContent }),
    });

    const result = await response.json();
    document.getElementById('result').innerHTML =
        `<p>SVC Result: ${result['SVC']}<p>
         <p>Naive Bayes Result: ${result['NB']}<p>
         <p>Rudimentary Naive Bayes Result: ${result['NB_scratch']}<p>`;
});

document.getElementById('stats-button').addEventListener('click', () => {
    const visible = document.getElementById('visible');
    if (visible.style.display === 'none')
        visible.style.display = 'block';
    else
        visible.style.display = 'none'
});

document.addEventListener('DOMContentLoaded', (event) => {
    const linksButton = document.getElementById('links-button');
    const linksContainer = document.getElementById('links-container');

    linksButton.addEventListener('click', () => {
        if (linksContainer.style.display === 'none') {
            linksContainer.style.display = 'block';
        } else {
            linksContainer.style.display = 'none';
        }
    });
});