my $client = AnyEvent::WebSocket::Client->new;

# server with raw data
$client->connect("wss://test-ws.skns.dev/raw-messages")->cb(sub {
  our $connection = eval { shift->recv };
  if($@) {
    print ("connection error");
    warn $@;
    return;
  }

  # recieve message from the websocket...
  $connection->on(each_message => sub {
    my($connection, $message) = @_;
    my $msg = $message->body;
    print ("GOT $msg\n");
  });


});

AnyEvent->condvar->recv;