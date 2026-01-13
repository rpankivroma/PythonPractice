const API_URL = '/api';


async function apiRequest(endpoint, method = 'GET', body = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    };
    if (body) options.body = JSON.stringify(body);

    try {
        const url = `${API_URL}${endpoint}`;
        const response = await fetch(url, options);
        if (!response.ok) {
            if (response.status === 401 && endpoint === '/me') return null;
            
            try {
                const err = await response.json();
                return { error: err.error || 'Request failed' };
            } catch (e) {
                return { error: `Server error: ${response.status}` };
            }
        }
        return await response.json();
    } catch (error) {
        console.error('API Request error:', error);
        return { error: 'Connection error' };
    }
}

async function checkAuth() {
    const user = await apiRequest('/me');
    if (user && !user.error) {
        updateNav(user);
        return user;
    }
    updateNav(null);
    return null;
}

function updateNav(user) {
    const loginLink = document.getElementById('login-link');
    const registerLink = document.getElementById('register-link');
    const logoutLink = document.getElementById('logout-link');
    const profileLink = document.getElementById('profile-link');
    
    if (user) {
        if (loginLink) loginLink.style.display = 'none';
        if (registerLink) registerLink.style.display = 'none';
        if (logoutLink) logoutLink.style.display = 'block';
        if (profileLink) profileLink.style.display = 'block';
    } else {
        if (loginLink) loginLink.style.display = 'block';
        if (registerLink) registerLink.style.display = 'block';
        if (logoutLink) logoutLink.style.display = 'none';
        if (profileLink) profileLink.style.display = 'none';
    }
}

async function logout() {
    await apiRequest('/logout', 'POST');
    window.location.href = '/';
}

document.addEventListener('DOMContentLoaded', async () => {
    setupAuthForms();
    await checkAuth();
});


function setupAuthForms() {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.onsubmit = async (e) => {
            e.preventDefault();
            const usernameInput = loginForm.querySelector('#login-username');
            const passwordInput = loginForm.querySelector('#login-password');
            
            const res = await apiRequest('/login', 'POST', { 
                username: usernameInput.value, 
                password: passwordInput.value 
            });
            
            if (res && !res.error) {
                window.location.reload();
            } else if (res && res.error) {
                alert(res.error);
            }
        };
    }

    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.onsubmit = async (e) => {
            e.preventDefault();
            const res = await apiRequest('/register', 'POST', { 
                username: document.getElementById('reg-username').value, 
                email: document.getElementById('reg-email').value, 
                password: document.getElementById('reg-password').value 
            });
            
            if (res && !res.error) {
                alert('Registration successful! Please login.');
                closeModal('registerModal');
                openModal('loginModal');
            } else if (res && res.error) {
                alert(res.error);
            }
        };
    }
}

window.apiRequest = apiRequest;
window.checkAuth = checkAuth;
window.logout = logout;
window.updateNav = updateNav;

document.addEventListener('DOMContentLoaded', () => {
    setupAuthForms();
});