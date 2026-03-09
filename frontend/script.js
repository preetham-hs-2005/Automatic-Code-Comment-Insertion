document.addEventListener('DOMContentLoaded', () => {
    const codeInput = document.getElementById('codeInput');
    const generateBtn = document.getElementById('generateBtn');
    const copyBtn = document.getElementById('copyBtn');
    const codeOutput = document.getElementById('codeOutput');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const toast = document.getElementById('toast');

    // Run syntax highlighting on load
    if (window.Prism) {
        Prism.highlightElement(codeOutput);
    }

    generateBtn.addEventListener('click', async () => {
        const sourceCode = codeInput.value;
        if (!sourceCode.trim()) return;

        // Show loading state
        loadingOverlay.classList.remove('hidden');
        generateBtn.disabled = true;
        generateBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Generating...';

        try {
            const response = await fetch('http://127.0.0.1:8001/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code: sourceCode })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();

            // Update UI
            codeOutput.textContent = data.commented_code;

            // Re-run syntax highlighting
            if (window.Prism) {
                Prism.highlightElement(codeOutput);
            }

        } catch (error) {
            console.error('Error generating comments:', error);
            codeOutput.textContent = '# Error connecting to the NLP backend.\n# Make sure the FastAPI server is running.\n' + error.message;
        } finally {
            // Hide loading state
            loadingOverlay.classList.add('hidden');
            generateBtn.disabled = false;
            generateBtn.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i> Generate Comments';
        }
    });

    copyBtn.addEventListener('click', () => {
        const textToCopy = codeOutput.textContent;
        navigator.clipboard.writeText(textToCopy).then(() => {
            // Show toast
            toast.classList.remove('hidden');
            setTimeout(() => {
                toast.classList.add('hidden');
            }, 3000);
        }).catch(err => {
            console.error('Failed to copy text: ', err);
        });
    });
});
