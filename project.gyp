#
#   This is the gyp script for libzmq
#
#   gyp --depth=.
{
  'targets': [
    {
      'target_name': 'libzmq',
      'type': 'static_library',
      'sources': [
        'include/zmq.h',
        'builds/gyp/platform.hpp',
        'src/address.cpp', 'src/address.hpp',
        'src/array.hpp',
        'src/atomic_counter.hpp',
        'src/atomic_ptr.hpp',
        'src/blob.hpp',
        'src/client.cpp', 'src/client.hpp',
        'src/clock.cpp', 'src/clock.hpp',
        'src/command.hpp',
        'src/condition_variable.hpp',
        'src/config.hpp',
        'src/ctx.cpp', 'src/ctx.hpp',
        'src/curve_client.cpp', 'src/curve_client.hpp',
        'src/curve_server.cpp', 'src/curve_server.hpp',
        'src/dbuffer.hpp',
        'src/dealer.cpp', 'src/dealer.hpp',
        'src/decoder.hpp',
        'src/devpoll.cpp', 'src/devpoll.hpp',
        'src/dish.cpp', 'src/dish.hpp',
        'src/dist.cpp', 'src/dist.hpp',
        'src/encoder.hpp',
        'src/epoll.cpp', 'src/epoll.hpp',
        'src/err.cpp', 'src/err.hpp',
        'src/fd.hpp',
        'src/fq.cpp', 'src/fq.hpp',
        'src/gssapi_mechanism_base.cpp', 'src/gssapi_mechanism_base.hpp',
        'src/gssapi_client.cpp', 'src/gssapi_client.hpp',
        'src/gssapi_server.cpp', 'src/gssapi_server.hpp',
        'src/i_encoder.hpp',
        'src/i_engine.hpp',
        'src/i_decoder.hpp',
        'src/i_mailbox.hpp',
        'src/i_poll_events.hpp',
        'src/io_object.cpp', 'src/io_object.hpp',
        'src/io_thread.cpp', 'src/io_thread.hpp',
        'src/ip.cpp', 'src/ip.hpp',
        'src/ipc_address.cpp', 'src/ipc_address.hpp',
        'src/ipc_connecter.cpp', 'src/ipc_connecter.hpp',
        'src/ipc_listener.cpp', 'src/ipc_listener.hpp',
        'src/kqueue.cpp', 'src/kqueue.hpp',
        'src/lb.cpp', 'src/lb.hpp',
        'src/likely.hpp',
        'src/mailbox.cpp', 'src/mailbox.hpp',
        'src/mailbox_safe.cpp', 'src/mailbox_safe.hpp',
        'src/mechanism.cpp', 'src/mechanism.hpp ',
        'src/metadata.cpp', 'src/metadata.hpp',
        'src/msg.cpp', 'src/msg.hpp',
        'src/mtrie.cpp', 'src/mtrie.hpp',
        'src/mutex.hpp',
        'src/norm_engine.cpp', 'src/norm_engine.hpp',
        'src/null_mechanism.cpp', 'src/null_mechanism.hpp',
        'src/object.cpp', 'src/object.hpp',
        'src/options.cpp', 'src/options.hpp',
        'src/own.cpp', 'src/own.hpp',
        'src/pair.cpp', 'src/pair.hpp',
        'src/pgm_receiver.cpp', 'src/pgm_receiver.hpp',
        'src/pgm_sender.cpp', 'src/pgm_sender.hpp',
        'src/pgm_socket.cpp', 'src/pgm_socket.hpp',
        'src/pipe.cpp', 'src/pipe.hpp',
        'src/plain_client.cpp', 'src/plain_client.hpp',
        'src/plain_server.cpp', 'src/plain_server.hpp',
        'src/poll.cpp', 'src/poll.hpp',
        'src/poller.hpp', 'src/poller_base.cpp',
        'src/poller_base.hpp',
        'src/proxy.cpp', 'src/proxy.hpp',
        'src/pub.cpp', 'src/pub.hpp',
        'src/pull.cpp', 'src/pull.hpp',
        'src/push.cpp', 'src/push.hpp',
        'src/radio.cpp', 'src/radio.hpp',
        'src/random.cpp', 'src/random.hpp',
        'src/raw_decoder.cpp', 'src/raw_decoder.hpp',
        'src/raw_encoder.cpp', 'src/raw_encoder.hpp',
        'src/reaper.cpp', 'src/reaper.hpp',
        'src/rep.cpp', 'src/rep.hpp',
        'src/req.cpp', 'src/req.hpp',
        'src/router.cpp', 'src/router.hpp',
        'src/select.cpp', 'src/select.hpp',
        'src/server.cpp', 'src/server.hpp',
        'src/session_base.cpp', 'src/session_base.hpp',
        'src/signaler.cpp', 'src/signaler.hpp',
        'src/socket_base.cpp', 'src/socket_base.hpp',
        'src/socks.cpp', 'src/socks.hpp',
        'src/socks_connecter.cpp', 'src/socks_connecter.hpp',
        'src/stdint.hpp',
        'src/stream.cpp', 'src/stream.hpp',
        'src/stream_engine.cpp', 'src/stream_engine.hpp',
        'src/sub.cpp', 'src/sub.hpp',
        'src/tcp.cpp', 'src/tcp.hpp',
        'src/tcp_address.cpp', 'src/tcp_address.hpp',
        'src/tcp_connecter.cpp', 'src/tcp_connecter.hpp',
        'src/tcp_listener.cpp', 'src/tcp_listener.hpp',
        'src/thread.cpp', 'src/thread.hpp',
        'src/timers.cpp', 'src/timers.hpp',
        'src/tipc_address.cpp', 'src/tipc_address.hpp',
        'src/tipc_connecter.cpp', 'src/tipc_connecter.hpp',
        'src/tipc_listener.cpp', 'src/tipc_listener.hpp',
        'src/trie.cpp', 'src/trie.hpp',
        'src/tweetnacl.c', 'src/tweetnacl.h',
        'src/udp_address.cpp', 'src/udp_address.hpp',
        'src/udp_engine.cpp', 'src/udp_engine.hpp',
        'src/v1_decoder.cpp', 'src/v1_decoder.hpp',
        'src/v2_decoder.cpp', 'src/v2_decoder.hpp',
        'src/v1_encoder.cpp', 'src/v1_encoder.hpp',
        'src/v2_encoder.cpp', 'src/v2_encoder.hpp',
        'src/v2_protocol.hpp',
        'src/vmci.cpp', 'src/vmci.hpp',
        'src/vmci_address.cpp', 'src/vmci_address.hpp',
        'src/vmci_connecter.cpp', 'src/vmci_connecter.hpp',
        'src/vmci_listener.cpp', 'src/vmci_listener.hpp',
        'src/windows.hpp',
        'src/wire.hpp',
        'src/xpub.cpp', 'src/xpub.hpp',
        'src/xsub.cpp', 'src/xsub.hpp',
        'src/ypipe.hpp',
        'src/ypipe_base.hpp',
        'src/ypipe_conflate.hpp',
        'src/yqueue.hpp',
        'src/zmq.cpp',
        'src/zmq_utils.cpp',
        'src/decoder_allocators.cpp', 'src/decoder_allocators.hpp',
        'src/socket_poller.cpp' 'src/socket_poller.hpp',
      ],
      'include_dirs': [
        'include',
        'builds/gyp'
      ],
      'conditions': [
        [ 'OS=="win"', {
            "defines": [
              "ZMQ_HAVE_WINDOWS"
            ]
        }],
        [ 'OS=="mac"', {
            "defines": [
              "ZMQ_HAVE_OSX"
            ]
        }],
        [ 'OS=="linux"', {
            "defines": [
              "ZMQ_HAVE_LINUX"
            ]
        }]
      ]
    }
  ]
}
