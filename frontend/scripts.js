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
    document.getElementById('result').innerText = `Result: ${result.classification}`;
});

document.getElementById('stats-button').addEventListener('click', () => {
    const visible = document.getElementById('visible');
    if (visible.style.display === 'none')
        visible.style.display = 'block';
    else
        visible.style.display = 'none'
});