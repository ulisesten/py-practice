
/********************************************/
/*////////////////////////////////////////////
Se debe crear primero la base de datos OrdenesPC
después ejecutar todo este script para crear tablas con sus relaciones
/////////////////////////////////////////////
*/
USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Dispositivo_Entrada]    Script Date: 8/9/2021 21:48:37 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Dispositivo_Entrada](
	[id_tipo_entrada] [smallint] IDENTITY(1,1) NOT NULL,
	[marca] [varchar](20) NOT NULL,
	[entrada] [varchar](10) NOT NULL,
 CONSTRAINT [PK_Tipo_Entrada] PRIMARY KEY CLUSTERED 
(
	[id_tipo_entrada] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Raton]    Script Date: 8/9/2021 21:51:24 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Raton](
	[id_raton] [smallint] IDENTITY(1,1) NOT NULL,
	[cantidad_botones] [smallint] NULL,
	[id_tipo_entrada] [smallint] NOT NULL,
 CONSTRAINT [PK_Raton] PRIMARY KEY CLUSTERED 
(
	[id_raton] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Raton]  WITH CHECK ADD  CONSTRAINT [FK_Raton_Tipo_Entrada] FOREIGN KEY([id_tipo_entrada])
REFERENCES [dbo].[Dispositivo_Entrada] ([id_tipo_entrada])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Raton] CHECK CONSTRAINT [FK_Raton_Tipo_Entrada]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Teclado]    Script Date: 8/9/2021 21:51:50 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Teclado](
	[id_teclado] [smallint] IDENTITY(1,1) NOT NULL,
	[idioma] [varchar](10) NULL,
	[id_tipo_entrada] [smallint] NOT NULL,
 CONSTRAINT [PK_Teclado] PRIMARY KEY CLUSTERED 
(
	[id_teclado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Teclado]  WITH CHECK ADD  CONSTRAINT [FK_Teclado_Tipo_Entrada] FOREIGN KEY([id_tipo_entrada])
REFERENCES [dbo].[Dispositivo_Entrada] ([id_tipo_entrada])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Teclado] CHECK CONSTRAINT [FK_Teclado_Tipo_Entrada]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Monitor]    Script Date: 8/9/2021 21:52:25 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Monitor](
	[id_monitor] [smallint] IDENTITY(1,1) NOT NULL,
	[marca] [varchar](20) NOT NULL,
	[tamano] [tinyint] NOT NULL,
 CONSTRAINT [PK_Monitor] PRIMARY KEY CLUSTERED 
(
	[id_monitor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Computador]    Script Date: 8/9/2021 21:52:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Computador](
	[id_computador] [smallint] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](20) NOT NULL,
	[id_raton] [smallint] NOT NULL,
	[id_teclado] [smallint] NOT NULL,
	[id_monitor] [smallint] NOT NULL,
 CONSTRAINT [PK_Computador] PRIMARY KEY CLUSTERED 
(
	[id_computador] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Computador]  WITH CHECK ADD  CONSTRAINT [FK_Computador_Monitor] FOREIGN KEY([id_monitor])
REFERENCES [dbo].[Monitor] ([id_monitor])
GO

ALTER TABLE [dbo].[Computador] CHECK CONSTRAINT [FK_Computador_Monitor]
GO

ALTER TABLE [dbo].[Computador]  WITH CHECK ADD  CONSTRAINT [FK_Computador_Raton] FOREIGN KEY([id_raton])
REFERENCES [dbo].[Raton] ([id_raton])
GO

ALTER TABLE [dbo].[Computador] CHECK CONSTRAINT [FK_Computador_Raton]
GO

ALTER TABLE [dbo].[Computador]  WITH CHECK ADD  CONSTRAINT [FK_Computador_Teclado] FOREIGN KEY([id_teclado])
REFERENCES [dbo].[Teclado] ([id_teclado])
GO

ALTER TABLE [dbo].[Computador] CHECK CONSTRAINT [FK_Computador_Teclado]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Persona]    Script Date: 8/9/2021 21:54:15 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Persona](
	[id_persona] [smallint] IDENTITY(1,1) NOT NULL,
	[cedula] [char](10) NOT NULL,
	[nombre] [varchar](20) NOT NULL,
	[apellido] [varchar](20) NOT NULL,
	[email] [varchar](100) NOT NULL,
	[direccion] [varchar](100) NULL,
	[telefono] [char](10) NULL,
 CONSTRAINT [PK_Persona] PRIMARY KEY CLUSTERED 
(
	[id_persona] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Orden]    Script Date: 8/9/2021 21:54:36 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Orden](
	[id_orden] [smallint] IDENTITY(1,1) NOT NULL,
	[id_persona] [smallint] NOT NULL,
	[fecha_hora] [nchar](10) NULL,
 CONSTRAINT [PK_Orden] PRIMARY KEY CLUSTERED 
(
	[id_orden] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Orden] ADD  CONSTRAINT [DF_Orden_fecha_hora]  DEFAULT (getdate()) FOR [fecha_hora]
GO

ALTER TABLE [dbo].[Orden]  WITH CHECK ADD  CONSTRAINT [FK_Orden_Persona] FOREIGN KEY([id_persona])
REFERENCES [dbo].[Persona] ([id_persona])
GO

ALTER TABLE [dbo].[Orden] CHECK CONSTRAINT [FK_Orden_Persona]
GO

USE [OrdenesPC]
GO

/****** Object:  Table [dbo].[Orden_Computador]    Script Date: 8/9/2021 21:55:07 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Orden_Computador](
	[id_computador] [smallint] NOT NULL,
	[id_orden] [smallint] NOT NULL,
 CONSTRAINT [PK_Orden_Computador] PRIMARY KEY CLUSTERED 
(
	[id_computador] ASC,
	[id_orden] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Orden_Computador]  WITH CHECK ADD  CONSTRAINT [FK_Orden_Computador_Computador] FOREIGN KEY([id_computador])
REFERENCES [dbo].[Computador] ([id_computador])
GO

ALTER TABLE [dbo].[Orden_Computador] CHECK CONSTRAINT [FK_Orden_Computador_Computador]
GO

ALTER TABLE [dbo].[Orden_Computador]  WITH CHECK ADD  CONSTRAINT [FK_Orden_Computador_Orden] FOREIGN KEY([id_orden])
REFERENCES [dbo].[Orden] ([id_orden])
GO

ALTER TABLE [dbo].[Orden_Computador] CHECK CONSTRAINT [FK_Orden_Computador_Orden]
GO

