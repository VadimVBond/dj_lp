document.addEventListener('DOMContentLoaded', () => {
    console.log('Theme toggle script initialized');

    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    if (!themeToggleBtn) {
        console.error('Theme toggle button NOT found in DOM');
        return;
    }

    // Function to update icons
    const updateIcons = (theme) => {
        if (theme === 'dark') {
            themeToggleLightIcon.classList.remove('hidden');
            themeToggleDarkIcon.classList.add('hidden');
        } else {
            themeToggleLightIcon.classList.add('hidden');
            themeToggleDarkIcon.classList.remove('hidden');
        }
    };

    // Set initial state
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    console.log('Current theme detected:', currentTheme);
    updateIcons(currentTheme);

    themeToggleBtn.addEventListener('click', function() {
        const theme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        updateIcons(theme);
        
        console.log('Theme toggled to:', theme);
    });
});