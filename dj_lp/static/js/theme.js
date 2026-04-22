(function() {
    const initTheme = () => {
        const themeToggleBtn = document.getElementById('themeToggle');
        const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
        const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

        if (!themeToggleBtn) return;

        const updateUI = (theme) => {
            if (theme === 'dark') {
                themeToggleLightIcon?.classList.remove('hidden');
                themeToggleDarkIcon?.classList.add('hidden');
                document.documentElement.setAttribute('data-theme', 'dark');
            } else {
                themeToggleLightIcon?.classList.add('hidden');
                themeToggleDarkIcon?.classList.remove('hidden');
                document.documentElement.setAttribute('data-theme', 'light');
            }
        };

        // Get initial theme from document attribute (set by head script)
        let theme = document.documentElement.getAttribute('data-theme') || 'light';
        updateUI(theme);

        themeToggleBtn.addEventListener('click', () => {
            theme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            localStorage.setItem('theme', theme);
            updateUI(theme);
        });
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }
})();
