import * as React from 'react';
import { Text, View, StyleSheet, Button, TouchableOpacity } from 'react-native';

const styles = StyleSheet.create({
    TableInfoHeader: {
        height: "15%",
        backgroundColor: "#13C0EB",
        alignContent: "center",
        justifyContent: "center"
    },
    TableInfoHeaderText: {
        color: "#ffffff",
        fontSize: 40,
        textAlign: "center",
    },
    TableInfoView: {
        height: "70%",
        backgroundColor: "#ffffff"
    },
    TableInfoFooter: {
        flexDirection: "row",
        height: "15%"
    },
    PayView: {
        backgroundColor: "#13C0EB",
        height: "100%",
        alignContent: "center",
        justifyContent: "center"
    },
    PayTouchable:{
        width: "50%",
        height: "100%",
    },
    PayText:{
        color: "#ffffff",
        fontSize: 25,
        textAlign: "center",
    },
    RequestView: {
        backgroundColor: "#292E30",
        height: "100%",
        alignContent: "center",
        justifyContent: "center"
    },
    RequestTouchable:{
        width: "50%",
        height: "100%",
    },
    RequestText:{
        color: "#ffffff",
        fontSize: 25,
        textAlign: "center",
    }
});

class CustomerView extends React.Component {
    render() {
        return (
            <View>
                <View style={styles.TableInfoHeader}>
                    <Text style={styles.TableInfoHeaderText}>
                        Table Information
                    </Text>
                </View>
                <View style={styles.TableInfoView}>
                    <Text>
                        Test
                    </Text>
                </View>
                <View style={styles.TableInfoFooter}>
                    <TouchableOpacity style={styles.RequestTouchable}>
                        <View style={styles.RequestView}>
                            <Text style={styles.RequestText}>
                                Request Server
                            </Text>
                        </View>
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.PayTouchable}>
                        <View style={styles.PayView}>
                            <Text style={styles.PayText}>
                                Pay
                            </Text>
                        </View>
                    </TouchableOpacity>
                </View>
            </View>
        )
    }
}

export default CustomerView;