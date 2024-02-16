function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");

    var userMessage = document.createElement("div");
    userMessage.classList.add("chat-message", "chat-message-user");
    userMessage.innerHTML = "<p>" + userInput + "</p>";
    chatBox.appendChild(userMessage);

    // Call your chatbot function here and get the response
    var botResponse = "This is a placeholder response from the chatbot.";

    var botMessage = document.createElement("div");
    botMessage.classList.add("chat-message", "chat-message-bot");
    botMessage.innerHTML = "<p>" + botResponse + "</p>";
    chatBox.appendChild(botMessage);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
