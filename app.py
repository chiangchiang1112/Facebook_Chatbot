from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "123456789"
machine = TocMachine(
    states=[
        'user','state1','state2','state3','state4','state5','state6','state7','state8','state9','state10','state11','state12','state13','state14','state15','state16','state17','state18','state19','state20','state21','state22','state23','state24','state25','state26','state27','state28','state29','state30','state31'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state14',
            'conditions': 'is_going_to_state14'
        },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state15',
            'conditions': 'is_going_to_state15'
        },
        {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state16',
            'conditions': 'is_going_to_state16'
        },
        {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state17',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state18',
            'conditions': 'is_going_to_state18'
        },
        {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state19',
            'conditions': 'is_going_to_state19'
        },
        {
            'trigger': 'advance',
            'source': 'state17',
            'dest': 'state20',
            'conditions': 'is_going_to_state20'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state24',
            'conditions': 'is_going_to_state24'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state25',
            'conditions': 'is_going_to_state25'
        },
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state26',
            'conditions': 'is_going_to_state26'
        },
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state27',
            'conditions': 'is_going_to_state27'
        },
        {
            'trigger': 'advance',
            'source': 'state27',
            'dest': 'state28',
            'conditions': 'is_going_to_state28'
        },
        {
            'trigger': 'advance',
            'source': 'state27',
            'dest': 'state29',
            'conditions': 'is_going_to_state29'
        },
        {
            'trigger': 'advance',
            'source': 'state28',
            'dest': 'state30',
            'conditions': 'is_going_to_state30'
        },
        {
            'trigger': 'advance',
            'source': 'state28',
            'dest': 'state31',
            'conditions': 'is_going_to_state31'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state3',
                'state6',
                'state7',
                'state9',
                'state10',
                'state12',
                'state14',
                'state16',
                'state18',
                'state19',
                'state20',
                'state24',
                'state25',
                'state26',
                'state29',
                'state30',
                'state31'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
