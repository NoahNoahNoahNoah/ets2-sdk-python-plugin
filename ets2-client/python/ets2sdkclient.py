import mmap
import struct

class ets2sdkclient:
    def update(self):
        self.mm = mmap.mmap(0, 1024, "Local\\SimTelemetryETS2")
        
        #[FieldOffset(0)]
        self.time = struct.unpack("I", self.mm[0:4])[0]
        #[FieldOffset(4)]
        self.paused = struct.unpack("I", self.mm[4:8])[0]
        
        
        #[FieldOffset(8)]
        self.ets2_telemetry_plugin_revision = struct.unpack("I", self.mm[8:12])[0]
        #[FieldOffset(12)]
        self.ets2_version_major = struct.unpack("I", self.mm[12:16])[0]
        #[FieldOffset(16)]
        self.ets2_version_minor = struct.unpack("I", self.mm[16:20])[0]
        
        #[FieldOffset(20)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        self.flags = self.mm[20:24]
        
        #[FieldOffset(24)]
        self.speed = struct.unpack("f", self.mm[24:28])[0]
        #[FieldOffset(28)]
        self.accelerationX = struct.unpack("f", self.mm[28:32])[0]
        #[FieldOffset(32)]
        self.accelerationY = struct.unpack("f", self.mm[32:36])[0]
        #[FieldOffset(36)]
        self.accelerationZ = struct.unpack("f", self.mm[36:40])[0]


        #[FieldOffset(40)]
        self.coordinateX  = struct.unpack("f", self.mm[40:44])[0]
        #[FieldOffset(44)]
        self.coordinateY  = struct.unpack("f", self.mm[44:48])[0]
        #[FieldOffset(48)]
        self.coordinateZ = struct.unpack("f", self.mm[48:52])[0]


        #[FieldOffset(52)]
        self.rotationX = struct.unpack("f", self.mm[52:56])[0]
        #[FieldOffset(56)]
        self.rotationY = struct.unpack("f", self.mm[56:60])[0]
        #[FieldOffset(60)]
        self.rotationZ = struct.unpack("f", self.mm[60:64])[0]
        
        #[FieldOffset(64)]
        self.gear = struct.unpack("I", self.mm[64:68])[0]
        #[FieldOffset(68)]
        self.gears = struct.unpack("I", self.mm[68:72])[0]
        #[FieldOffset(72)]
        self.gearRanges = struct.unpack("I", self.mm[72:76])[0]
        #[FieldOffset(76)]
        self.gearRangeActive = struct.unpack("I", self.mm[76:80])[0]

        #[FieldOffset(80)]
        self.engineRpm = struct.unpack("f", self.mm[80:84])[0]
        #[FieldOffset(84)]
        self.engineRpmMax = struct.unpack("f", self.mm[84:88])[0]

        #[FieldOffset(88)]
        self.fuel = struct.unpack("f", self.mm[88:92])[0]
        #[FieldOffset(92)]
        self.fuelCapacity = struct.unpack("f", self.mm[92:96])[0]
        #[FieldOffset(96)]
        self.fuelRate = struct.unpack("f", self.mm[96:100])[0]
        #[FieldOffset(100)]
        self.fuelAvgConsumption = struct.unpack("f", self.mm[100:104])[0]
        
        #[FieldOffset(104)]
        self.userSteer = struct.unpack("f", self.mm[104:108])[0]
        #[FieldOffset(108)]
        self.userThrottle = struct.unpack("f", self.mm[108:112])[0]
        #[FieldOffset(112)]
        self.userBrake = struct.unpack("f", self.mm[112:116])[0]
        #[FieldOffset(116)]
        self.userClutch = struct.unpack("f", self.mm[116:120])[0]


        #[FieldOffset(120)]
        self.gameSteer = struct.unpack("f", self.mm[120:124])[0]
        #[FieldOffset(124)]
        self.gameThrottle = struct.unpack("f", self.mm[124:128])[0]
        #[FieldOffset(128)]
        self.gameBrake = struct.unpack("f", self.mm[128:132])[0]
        #[FieldOffset(132)]
        self.gameClutch = struct.unpack("f", self.mm[132:136])[0]
        
        
        #[FieldOffset(136)]
        self.truckWeight = struct.unpack("f", self.mm[136:140])[0]
        #[FieldOffset(140)]
        self.trailerWeight = struct.unpack("f", self.mm[140:144])[0]

        #[FieldOffset(144)]
        self.modelOffset = struct.unpack("I", self.mm[144:148])[0]
        #[FieldOffset(148)]
        self.modelLength = struct.unpack("I", self.mm[148:152])[0]

        #[FieldOffset(152)]
        self.trailerOffset = struct.unpack("I", self.mm[152:156])[0]
        #[FieldOffset(156)]
        self.trailerLength = struct.unpack("I", self.mm[156:160])[0]
        
        #[FieldOffset(160)]
        self.timeAbsolute = struct.unpack("I", self.mm[160:164])[0]
        #[FieldOffset(164)]
        self.gearsReverse = struct.unpack("I", self.mm[164:168])[0]

        #[FieldOffset(168)]
        self.trailerMass = struct.unpack("f", self.mm[168:172])[0]
        
        #[FieldOffset(172)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.trailerId = self.mm[172:236]
        
        #[FieldOffset(236)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self. trailerName = self.mm[236:300]

        #[FieldOffset(300)]
        self.jobIncome = struct.unpack("I", self.mm[300:304])[0]
        #[FieldOffset(304)]
        self.jobDeadline = struct.unpack("I", self.mm[304:308])[0]

        #[FieldOffset(308)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.jobCitySource = self.mm[308:372]
        
        #[FieldOffset(372)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.jobCityDestination = self.mm[372:436]

        #[FieldOffset(436)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.jobCompanySource = self.mm[436:500]
        
        #[FieldOffset(500)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.jobCompanyDestination = self.mm[500:564]
        
        #[FieldOffset(564)]
        self.retarderBrake = struct.unpack("I", self.mm[564:568])[0]
        #[FieldOffset(568)]
        self.shifterSlot = struct.unpack("I", self.mm[568:572])[0]
        #[FieldOffset(572)]
        self.shifterToggle = struct.unpack("I", self.mm[572:576])[0]
        #//#[FieldOffset(576)]
        #//self.fill;
        
        #[FieldOffset(580)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 24)]
        self.aux = self.mm[580:604]
        #[FieldOffset(604)]
        self.airPressure = struct.unpack("f", self.mm[604:608])[0]
        #[FieldOffset(608)]
        self.brakeTemperature = struct.unpack("f", self.mm[608:612])[0]
        #[FieldOffset(612)]
        self.fuelWarning = struct.unpack("I", self.mm[612:616])[0]
        #[FieldOffset(616)]
        self.adblue = struct.unpack("f", self.mm[616:620])[0]
        #[FieldOffset(620)]
        self.adblueConsumption = struct.unpack("f", self.mm[620:624])[0]
        #[FieldOffset(624)]
        self.oilPressure = struct.unpack("f", self.mm[624:628])[0]
        #[FieldOffset(628)]
        self.oilTemperature = struct.unpack("f", self.mm[628:632])[0]
        #[FieldOffset(632)]
        self.waterTemperature = struct.unpack("f", self.mm[632:636])[0]
        #[FieldOffset(636)]
        self.batteryVoltage = struct.unpack("f", self.mm[636:640])[0]
        #[FieldOffset(640)]
        self.lightsDashboard = struct.unpack("f", self.mm[640:644])[0]
        #[FieldOffset(644)]
        self.wearEngine = struct.unpack("f", self.mm[644:648])[0]
        #[FieldOffset(648)]
        self.wearTransmission = struct.unpack("f", self.mm[648:652])[0]
        #[FieldOffset(652)]
        self.wearCabin = struct.unpack("f", self.mm[652:656])[0]
        #[FieldOffset(656)]
        self.wearChassis = struct.unpack("f", self.mm[656:660])[0]
        #[FieldOffset(660)]
        self.wearWheels = struct.unpack("f", self.mm[660:664])[0]
        #[FieldOffset(664)]
        self.wearTrailer = struct.unpack("f", self.mm[664:668])[0]
        #[FieldOffset(668)]
        self.truckOdometer = struct.unpack("f", self.mm[668:672])[0]
        #[FieldOffset(672)]
        self.cruiseControlSpeed = struct.unpack("f", self.mm[672:676])[0]

        #[FieldOffset(676)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.truckMake = self.mm[676:740]
        #[FieldOffset(740)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.truckMakeId = self.mm[740:804]
        #[FieldOffset(804)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        self.truckModel = self.mm[804:868]

        #[FieldOffset(868)]
        self.speedLimit = struct.unpack("f", self.mm[868:872])[0]

        #[FieldOffset(872)]
        self.routeDistance = struct.unpack("f", self.mm[872:876])[0]

        #[FieldOffset(876)]
        self.routeTime = struct.unpack("f", self.mm[876:880])[0]

        #[FieldOffset(880)]
        self.fuelRange = struct.unpack("f", self.mm[880:884])[0]

        #[FieldOffset(884)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 24)]
        #public float[] gearRatioForward;

        #[FieldOffset(980)]
        #[MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        #public float[] gearRatioReverse;

        #[FieldOffset(1012)]
        self.gearRatioDifferential = struct.unpack("f", self.mm[1012:1016])[0]

        #[FieldOffset(1016)]
        self.gearDashboard  = struct.unpack("I", self.mm[1016:1020])[0]
        
        self.mm.close()
        
    def printall(self):
        attrs = vars(self)
        # {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
        # now dump this in some way or another
        print ', \n'.join("%s: %s" % item for item in attrs.items())

e = ets2sdkclient()
e.update()
e.printall()