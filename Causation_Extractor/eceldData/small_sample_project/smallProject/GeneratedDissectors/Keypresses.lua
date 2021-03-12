-- Keypresses frame number-based postdissector
-- declare Fields to be read
-- declare our (pseudo) protocol
Keypresses_proto = Proto("keypresses","Keypresses Log")
-- create the fields for our "protocol"
timestamp_F = ProtoField.string("keypresses.timestamp","Original Event Timestamp")
eventdata_F = ProtoField.string("keypresses.data","Log Data")

-- add the field to the protocol
Keypresses_proto.fields = {timestamp_F, eventdata_F}

-- create a function to "postdissect" each frame
function Keypresses_proto.dissector(buffer,pinfo,tree)
    -- add the data based on timestamps
    if pinfo.abs_ts >= 1615326278.0 and pinfo.abs_ts <= 1615326280.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("sudo ifconfig[Return]ping 10.0.2.1[Return][Control_L]c")

       subtree:add(timestamp_F,tostring("2021-03-09T21:44:38"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1615326283.0 and pinfo.abs_ts <= 1615326285.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("ping 10.0.2.18")

       subtree:add(timestamp_F,tostring("2021-03-09T21:44:43"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1615326331.0 and pinfo.abs_ts <= 1615326333.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Return][Control_L]c")

       subtree:add(timestamp_F,tostring("2021-03-09T21:45:31"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1615326336.0 and pinfo.abs_ts <= 1615326338.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("sudo ls[Return]")

       subtree:add(timestamp_F,tostring("2021-03-09T21:45:36"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1615326343.0 and pinfo.abs_ts <= 1615326345.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("print [Shift_L]'done here[Shift_L]:[Return][Shift_L]'")

       subtree:add(timestamp_F,tostring("2021-03-09T21:45:43"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(Keypresses_proto)