document.addEventListener('DOMContentLoaded', () => {
    const html = document.getElementById('html');
    const toggleBtn = document.getElementById('toggleDark');
    const modelMenu = document.getElementById('modelDropdownMenu');
    const modelButton = document.getElementById('modelDropdownButton');
    const modelInput = document.getElementById('modelInput');
    const selectedModelSpan = document.getElementById('selectedModel');
    const dropdownIcon = document.getElementById('dropdownIcon');
    const historyDiv = document.getElementById('conversationHistory');
    const inputText = document.getElementById('inputText');
    const loading = document.getElementById('loading');
    const submitBtn = document.getElementById('submitBtn');

    function updateDarkModeIcon() {
        toggleBtn.textContent = html.classList.contains('dark') ? '🌙' : '☀️';
    }

    toggleBtn.addEventListener('click', () => {
        html.classList.toggle('dark');
        updateDarkModeIcon();
    });

    function toggleDropdown(forceClose = false) {
        const open = !forceClose && modelMenu.classList.contains('hidden');
        modelMenu.classList.toggle('hidden', !open);
        dropdownIcon.classList.toggle('rotate-180', open);
    }

    document.addEventListener('click', (e) => {
        if (!document.getElementById('modelDropdownWrapper').contains(e.target)) {
            toggleDropdown(true);
        }
    });

    function selectModel(model) {
        selectedModelSpan.textContent = model;
        modelInput.value = model;
        toggleDropdown(true);
        document.title = `DeepSeek - ${model}`;
    }

    function loadModels() {
        fetch('/get-models')
            .then(res => res.json())
            .then(data => {
                modelMenu.innerHTML = '';
                data.models.forEach((model, i) => {
                    const item = document.createElement('div');
                    item.className = "px-4 py-2 text-sm cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-900 dark:text-gray-100";
                    item.textContent = model;
                    item.addEventListener('click', () => selectModel(model));
                    modelMenu.appendChild(item);
                    if (i === 0) selectModel(model);
                });
            })
            .catch(err => console.error('Error loading models:', err));
    }

    modelButton.addEventListener('click', () => toggleDropdown());

    loadModels();
    updateDarkModeIcon();
    inputText.focus();

    inputText.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            document.getElementById('queryForm').requestSubmit();
        }
    });

    document.getElementById('queryForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = inputText.value.trim();
        if (!query) return;
        inputText.value = '';
        const formData = new FormData(e.target);
        formData.append('model', modelInput.value);

        loading.classList.remove('hidden');
        submitBtn.disabled = true;

        const userMsg = document.createElement('div');
        userMsg.className = "mb-4 self-start bg-gray-300 dark:bg-gray-800 p-3 rounded-md";
        userMsg.innerHTML = `<strong class="block text-indigo-600 dark:text-indigo-400 mb-1">You:</strong><p>${query}</p>`;
        historyDiv.appendChild(userMsg);

        const res = await fetch('/query-ai', {method: 'POST', body: formData});
        const data = await res.json();
        const cleanResponse = data.response.replace(/<think>/gi, '').replace(/<\/think>/gi, '');

        const aiMsg = document.createElement('div');
        aiMsg.className = "mb-4 self-start bg-gray-200 dark:bg-gray-700 p-3 rounded-md prose prose-sm dark:prose-invert max-w-none";
        aiMsg.innerHTML = `<strong class="block text-green-600 dark:text-green-400 mb-1">AI:</strong>${marked.parse(cleanResponse)}`;
        historyDiv.appendChild(aiMsg);

        loading.classList.add('hidden');
        submitBtn.disabled = false;
        inputText.value = '';
        inputText.blur();
        inputText.focus();
        historyDiv.scrollTop = historyDiv.scrollHeight;
    });
});
