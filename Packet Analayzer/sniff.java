import jpcap.*;
import jpcap.NetworkInterface;

import jpcap.packet.DatalinkPacket;
import jpcap.packet.EthernetPacket;
import jpcap.packet.ICMPPacket;
import jpcap.packet.IPPacket;
import jpcap.packet.Packet;
import jpcap.packet.TCPPacket;
import jpcap.packet.UDPPacket;
import java.util.Scanner;


class Sniffer implements PacketReceiver{
    /**
     * @param type_of_packet:   This field conatins the information about which packet type you want to track. Eg. TCP.
     * @param protocoll:        This is an array consisting of all protocols linked with the protocol field of the packet.
     */
    static String type_of_packet = "TCP";
    static String protocoll[] = {"HOPOPT", "ICMP", "IGMP", "GGP", "IPV4", "ST", "TCP", "CBT", "EGP", "IGP", "BBN", "NV2", "PUP", "ARGUS", "EMCON", "XNET", "CHAOS", "UDP", "mux"};

    public void receivePacket(Packet packet){
        System.out.println(packet);

        IPPacket ip_packet = (IPPacket) packet;

        /**
         * Following are the fields that I used from IP Packet.
         * 
         * protocol:    This provides an integer corresponding to protocol type. This is linked with protocoll array to get actual type of protocol.
         * dont_frag:   This is a boolean value, says if the DO NOT FRAGMENT bit is set/not set.
         * src_ip:      Source IP Address.
         * dst_ip:      Destination IP address.
         * hop_limit:   Gives hop count.
         * priority:    Gives priority.
         * rsv_tos:     Type of service included in packet header.
         * r_flag:      Specifies if the connection used is reliable or not.
         * version:     Protocol version.
         */
        
        if(packet!=null){
            int protocol_number = ip_packet.protocol;
            String protocol = protocoll[protocol_number];
            if(type_of_packet.equals("All") || protocol.equals(type_of_packet)){
                System.out.println("---------- From Network Layer ----------\n");
                if(ip_packet.dont_frag){
                    System.out.println("\n\tDo not fragment bit is set. Packet may not be fragmented.");
                }else{
                    System.out.println("\n\tDo not fragment bit is not set. The packet may be fragmented.");
                }
                System.out.println("\n\tSource IP Address: "+ip_packet.src_ip);
                System.out.println("\n\tDestination IP Address: "+ip_packet.dst_ip);
                System.out.println("\n\tHop count: "+ip_packet.hop_limit);
                System.out.println("\n\tPacket length: "+ip_packet.length);
                System.out.println("\n\tPacket priority: "+(int)ip_packet.priority);
                System.out.println("\n\tType of service: "+ip_packet.rsv_tos);
                if(ip_packet.r_flag){
                    System.out.println("\n\tPacket uses reliable transmission.");
                }else{
                    System.out.println("\n\tPacket uses unreliable transmission.");
                }
                System.out.println("\n\tProtocol version: "+(int)ip_packet.version);

                if (protocol.equals(("TCP"))) {
                    /**
                     * Documentation for fields used from TCP Packet
                     * 
                     * dst_port:    Destination port number.
                     * version:     TCP Version.
                     * dst_ip:      Destination IP Address.
                     * src_ip:      Source IP Address.
                     * 
                     * -- Flag based fields --
                     * ack: Boolean value stating if ACK (Is Acknowledgement?) flag is set in TCP Header.
                     * fin: Boolean value stating if FIN (Is Last packet?) flag is set in TCP Header.
                     * syn: Boolean value stating if SYN (Is Synchronisation packet?) flag is set in TCP Header.
                     */

                    TCPPacket tp = (TCPPacket) packet;
                    
                    System.out.println("\n\t```````````` TCP packet ````````````");
                    System.out.println("\n\tDestination port: " + tp.dst_port);

                    if (tp.ack) System.out.println("\n\tThis is an acknowledgement packet");
                    else System.out.println("\n\tThis is not an acknowledgment packet");

                    if (tp.rst) System.out.println("Connection reset packet");

                    System.out.println("\n\tProtocol version: " + tp.version);
                    System.out.println("\n\tDestination IP Address: " + tp.dst_ip);
                    System.out.println("\n\tSource IP Address: "+tp.src_ip);

                    if(tp.fin) System.out.println("\n\tNo more packets to be transferred. Finish bit is set.");
                    if(tp.syn) System.out.println("\n\tThis is a request for connection.");

                }
                else if(protocol.equals("ICMP")){
                    /**
                     * Documentation for fields used from ICMP Packet
                     * 
                     * alive_time:  TTL field value.
                     * subnetmask:  Subnet Mask used.
                     * src_ip:      Source IP Address.
                     * dst_ip:      Destination IP Address.
                     * checksum:    Checksum value from Header.
                     */

                    ICMPPacket ipc=(ICMPPacket)packet;
                    
                    System.out.println("\n\t```````````` ICMP packet ````````````");
                    System.out.println("\n\tTTL time: "+ipc.alive_time);
                    System.out.println("\n\tSubnet mask: "+ipc.subnetmask);
                    System.out.println("\n\tSource IP address: "+ipc.src_ip);
                    System.out.println("\n\tDestination IP address: "+ipc.dst_ip);
                    System.out.println("\n\tChecksum: "+ipc.checksum);
                }
                else if(protocol.equals("UDP")){
                    /**
                     * Documentation for fields used from UDP Packet
                     * 
                     * src_port: Contains Source Port number.
                     * dst_port: Contains Destination port number.
                     */

                    UDPPacket pac=(UDPPacket)packet;

                    System.out.println("\n\t```````````` UDP packet ````````````");
                    System.out.println("\n\tSource port: "+pac.src_port);
                    System.out.println("\n\tDestination port: "+pac.dst_port);
                }

                System.out.println("\n--------------------- From Datalink layer ---------------------");
                DatalinkPacket dp = packet.datalink;

                EthernetPacket ept=(EthernetPacket)dp;

                /**
                 * Documentation for methods used from EthernetPacket class.
                 * 
                 * getSourceAddress():      Returns source address of packet.
                 * getDestinationAddress(): Returns Destination address of packet.
                 */
                System.out.println("\n\tSource MAC Address: "+ept.getSourceAddress());
                System.out.println("\n\tDestination MAC Address: "+ept.getDestinationAddress());
            }
        }
    }

    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        NetworkInterface[] devices = JpcapCaptor.getDeviceList();

        for (int i = 0; i < devices.length; i++) {
            System.out.println(i + " :" + devices[i].name + "(" + devices[i].description + ")");
            System.out.println("    data link:" + devices[i].datalink_name + "("
                    + devices[i].datalink_description + ")");
            System.out.print("    MAC address:");
            for (byte b : devices[i].mac_address) {
                System.out.print(Integer.toHexString(b & 0xff) + ":");
            }
            System.out.println();
            for (NetworkInterfaceAddress a : devices[i].addresses) {
                System.out.println("    address:" + a.address + " " + a.subnet + " "
                        + a.broadcast);
            }
        }

        System.out.println("Total "+protocoll.length+" protocols.");
        System.out.println("Below are all Network Layer protocols which can be sniffed: ");
        int i=1;
        for(String each_protocol: protocoll){
            System.out.println(i++ + ": "+each_protocol);
        }
        System.out.println(i + ": All");
        while(true){
            System.out.print("\nEnter the index for your desired protocol: ");
            int index = sc.nextInt();
            if(index <= protocoll.length){
                type_of_packet = protocoll[index-1];
                break;
            }
            else if(index == protocoll.length + 1){
                type_of_packet = "All";
                break;
            }
            System.out.println("Sorry. Please refer the above table and re-enter your index.");
        }

        System.out.println("Type of packets to be sniffed: "+type_of_packet+"\n");

        System.out.println("\n--------------------- Packet sniffing starts now ---------------------");
        JpcapCaptor jpcap = JpcapCaptor.openDevice(devices[1], 2000, true, 20);
        jpcap.loopPacket(-1, new Sniffer());
    }
}
 /*
 Output format for one packet:

 1500889556:497506 /fe80:0:0:0:3862:2ae:4742:a286->/ff02:0:0:0:0:0:1:2 protocol(1
7) priority(0) flowlabel(1610612736) hop(1) UDP 546 > 547
---------- From Network Layer ----------


        Do not fragment bit is not set. The packet may be fragmented.

        Source IP Address: /fe80:0:0:0:3862:2ae:4742:a286

        Destination IP Address: /ff02:0:0:0:0:0:1:2

        Hop count: 1

        Packet length: 100

        Packet priority: 0

        Type of service: 0

        Packet uses unreliable transmission.

        Protocol version: 6

        ```````````` UDP packet ````````````

        Source port: 546

        Destination port: 547

--------------------- From Datalink layer ---------------------

        Source MAC Address: 00:50:56:c0:00:01

        Destination MAC Address: 33:33:00:01:00:02
*/