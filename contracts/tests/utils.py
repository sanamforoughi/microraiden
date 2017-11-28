from utils.sign import eth_signed_typed_data_message


def balance_proof_hash(receiver, block, balance):
    return eth_signed_typed_data_message(
        ('address', ('uint', 32), ('uint', 192)),
        ('receiver', 'block_created', 'balance'),
        (receiver, block, balance)
    )


def print_logs(contract, event, name=''):
    transfer_filter_past = contract.pastEvents(event)
    past_events = transfer_filter_past.get()
    if len(past_events):
        print('--(', name, ') past events for ', event, past_events)

    transfer_filter = contract.on(event)
    events = transfer_filter.get()
    if len(events):
        print('--(', name, ') events for ', event, events)

    transfer_filter.watch(lambda x: print('--(', name, ') event ', event, x['args']))
