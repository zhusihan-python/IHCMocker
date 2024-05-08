import QtQuick 6.7
import QtQuick.Window 6.7
import QtQuick.Controls 6.7
// import Qt.labs.platform 1.1
// import QtQuick.Layouts 1.5
// import QtQuick.Shapes 1.6
// import QtQuick.Timeline 1.0

Window {
    id: mainWindow
    width: 800
    height: 600
    visible: true
    // color: "#f1f2f3"
    title: qsTr("免疫组化模拟器")

    MouseArea {
        anchors.fill: parent;
        property variant clickPos: "1,1"

        onPressed: (mouse)=>{
            clickPos = Qt.point(mouse.x,mouse.y)
        }

        onPositionChanged: (mouse)=>{
            let delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y);
            let new_x = mainWindow.x + delta.x;
            let new_y = mainWindow.y + delta.y;
            mainWindow.x = new_x;
            mainWindow.y = new_y;
        }
    }
}