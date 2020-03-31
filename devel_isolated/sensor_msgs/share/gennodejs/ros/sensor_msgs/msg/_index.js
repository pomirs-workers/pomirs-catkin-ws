
"use strict";

let JoyFeedback = require('./JoyFeedback.js');
let JointState = require('./JointState.js');
let LaserEcho = require('./LaserEcho.js');
let Illuminance = require('./Illuminance.js');
let Joy = require('./Joy.js');
let LaserScan = require('./LaserScan.js');
let CameraInfo = require('./CameraInfo.js');
let PointCloud2 = require('./PointCloud2.js');
let ChannelFloat32 = require('./ChannelFloat32.js');
let Temperature = require('./Temperature.js');
let NavSatFix = require('./NavSatFix.js');
let Imu = require('./Imu.js');
let MagneticField = require('./MagneticField.js');
let PointField = require('./PointField.js');
let Image = require('./Image.js');
let MultiDOFJointState = require('./MultiDOFJointState.js');
let CompressedImage = require('./CompressedImage.js');
let RegionOfInterest = require('./RegionOfInterest.js');
let FluidPressure = require('./FluidPressure.js');
let RelativeHumidity = require('./RelativeHumidity.js');
let MultiEchoLaserScan = require('./MultiEchoLaserScan.js');
let TimeReference = require('./TimeReference.js');
let BatteryState = require('./BatteryState.js');
let JoyFeedbackArray = require('./JoyFeedbackArray.js');
let PointCloud = require('./PointCloud.js');
let Range = require('./Range.js');
let NavSatStatus = require('./NavSatStatus.js');

module.exports = {
  JoyFeedback: JoyFeedback,
  JointState: JointState,
  LaserEcho: LaserEcho,
  Illuminance: Illuminance,
  Joy: Joy,
  LaserScan: LaserScan,
  CameraInfo: CameraInfo,
  PointCloud2: PointCloud2,
  ChannelFloat32: ChannelFloat32,
  Temperature: Temperature,
  NavSatFix: NavSatFix,
  Imu: Imu,
  MagneticField: MagneticField,
  PointField: PointField,
  Image: Image,
  MultiDOFJointState: MultiDOFJointState,
  CompressedImage: CompressedImage,
  RegionOfInterest: RegionOfInterest,
  FluidPressure: FluidPressure,
  RelativeHumidity: RelativeHumidity,
  MultiEchoLaserScan: MultiEchoLaserScan,
  TimeReference: TimeReference,
  BatteryState: BatteryState,
  JoyFeedbackArray: JoyFeedbackArray,
  PointCloud: PointCloud,
  Range: Range,
  NavSatStatus: NavSatStatus,
};
