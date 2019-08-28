"""
This file only acts to serve as a list of properties associated with eact object related to a 
transaction. This is not to be runnable code. Eventually this will be deleted once replaced 
with functional objects.
"""
Transaction = {
    transaction_id
    location_id
    user_id
    array_of_items
    time_date_of_transaction # datetime should be recorded. Want it all the way down to the second.
    location_coords_of_transaction # if this is empty, then it should default to the company location.
}

Items = {
    item_id
    transaction_id
    item_name
    item_common_name
    item_cost

}

Company = {
    company_id
    company_name

}

Location = {
    location_id
    company_id
    location_coords
}

User = {
    user_id
}