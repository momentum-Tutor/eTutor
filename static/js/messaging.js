console.log('hello')

let $chatWindow = $("#messages");
let chatClient;
let roomChannel;
let username;

function printInfo(infoMessage, asHtml) {
    let $msg = $('<div class="info">');
    if (asHtml) {
    $msg.html(infoMessage);
    } else {
    $msg.text(infoMessage);
    }
    $chatWindow.append($msg);
}

function printMessage(fromUser, message) {
    let $user = $('<span class="username">').text(fromUser + ":");
    if (fromUser === username) {
    $user.addClass("me");
    }
    let $message = $('<p class="message">').text(message);
    let $container = $('<div class="message-container">');
    $container.append($user).append($message);
    $chatWindow.append($container);
    $chatWindow.scrollTop($chatWindow[0].scrollHeight);
}

$.getJSON(
    "/token",
    {
    device: "browser"
    },
    function(data) {
    // Alert the user they have been assigned a random username
    username = data.identity;
    printInfo(
        "You have been assigned a random username of: " +
        '<span class="me">' +
        username +
        "</span>",
        true
    );

    // Initialize the Chat client
    Twilio.Chat.Client.create(data.token).then(client => {
        // Use client
        chatClient = client;
        console.log(chatClient)
        chatClient.getSubscribedChannels().then(createOrJoinChannel);
    });

    }
    );

function createOrJoinChannel() {
    // Extract the room's channel name from the page URL
    let channelName = window.location.pathname.split("/").slice()[2]
  
   printInfo(`Attempting to join the "${channelName}" chat channel...`);
  
    chatClient
      .getChannelByUniqueName(channelName)
      .then(function(channel) {
        roomChannel = channel;
        setupChannel(channelName);
      })
      .catch(function() {
        // If it doesn't exist, let's create it
        chatClient
          .createChannel({
            uniqueName: channelName,
            friendlyName: `${channelName} Chat Channel`
          })
          .then(function(channel) {
            roomChannel = channel;
            setupChannel(channelName);
          });
      });
  }

  // Set up channel after it has been found / created
function setupChannel(name) {
    if (roomChannel.state.status == 'joined') {
        console.log('already joined')
        roomChannel.getMessages(30).then(processPage)
    } else { roomChannel.join().then(function(channel) {
      printInfo(
        `Joined channel ${name} as <span class="me"> ${username} </span>.`,
        true
      );
      channel.getMessages(30).then(processPage);
    });
}
  
    // Listen for new messages sent to the channel
    roomChannel.on("messageAdded", function(message) {
      printMessage(message.author, message.body);
    });
  }
  function processPage(page) {
    page.items.forEach(message => {
      printMessage(message.author, message.body);
    });
    if (page.hasNextPage) {
      page.nextPage().then(processPage);
    } else {
      console.log("Done loading messages");
    }
  }

  // Add newly sent messages to the channel
let $form = $("#message-form");
let $input = $("#message-input");
$form.on("submit", function(e) {
  e.preventDefault();
  if (roomChannel && $input.val().trim().length > 0) {
    roomChannel.sendMessage($input.val());
    $input.val("");
  }
});